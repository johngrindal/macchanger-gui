#import modules
from Tkinter import *
import tkMessageBox
from array import *
from tkFileDialog import askopenfilename
import getpass
import sys
import os
if not os.geteuid()==0:
    sys.exit("Please run this script as root")
selected = "none"
status = ""
from uuid import getnode as get_mac
textle = os.listdir('/sys/class/net/')
length = len(textle)


def install():
    print (":::checking for and installing missing packages:::")
    os.system('clear')
    
    #install macchanger if missing
    os.system('sudo apt-get install macchanger')
    os.system('yum install macchanger')
    
    
def update():
    status_label.config(text="status: %s" %(status))
    selected_label.config(text="Interface: %s" %(selected))
    root.after(1000, update)

    
def change_random():
    global status
    status = "changing..."
    os.system('clear')
    os.system('ifconfig %s down'%(selected))
    os.system('sudo macchanger --random %s'%(selected))
    os.system('ifconfig %s up'%(selected))
    status = "changed"
    update()
def change_certain():
    global status
    status = "changing..."
    os.system('clear')
    os.system('ifconfig %s down'%(selected))
    os.system("macchanger --mac=%s %s" %(entered, selected))
    os.system('ifconfig %s up' %(selected))
    status = "changed"
    
    

    
    
def donothing():
    print "Doingnothing"

def settle():
    selected = textle[counter]
    print selected

def one():
    
    global selected
    selected = textle[0]
    print selected
def two():
    global selected
    selected = textle[1]
    print selected
def three():
    global selected
    selected = textle[2]
    print selected
def four():
    global selected
    selected = textle[3]
    print selected
def five():
    global selected
    selected = textle[4]
    print selected
def six():
    global selected
    selected = textle[5]
    print selected






#make root for window
root = Tk()
install()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
options_menu = Menu(menubar, tearoff=0)
counter = 0
counter2 = 0
commands = [one, two, three, four, five, six]
for i in range(0, length):
    filemenu.add_command(label=textle[counter], command=commands[counter])
    counter += 1
    counter2 += 1
filemenu.add_separator()

menubar.add_cascade(label="Interfaces", menu=filemenu)
menubar.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="exit", command=sys.exit)


entry_label_1 = Label(root, bg="black", padx="5", fg="white", text="Change mac address")
entry_label_1.pack(fill=X)

selected_label = Label(root, bg="black",padx="5", fg="white", text="Interface : %s" %(selected))
selected_label.pack(fill=X)
new_mac_entry = Entry(root)
new_mac_entry.pack(fill=X)
entered = new_mac_entry.get()

random_mac_button = Button(root, bg="grey", fg="white",  text="Press for random mac address", command=change_random)
random_mac_button.pack(fill=X)

press = Button(root, bg="grey", fg="white", text="press to change mac address", command=change_certain)
press.pack(fill=X)

status_label = Label(root, text="status: %s" %(status))
status_label.pack(fill=X)


string = ("macchanger --mac=%s %s" %(entered, selected))
#finish off window
new_mac_entry.insert(0, 'type new mac address here')
root.after(1000, update)
root.configure(background="grey")
root.title('Mac Address Changer')
root.geometry('500x150')
root.config(menu=menubar)
root.mainloop()




    
