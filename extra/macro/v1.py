#Lucas 5 Dec 2022

import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import pynput.keyboard as keyboard
import pynput.mouse as mouse #Listener, Button
import time as t
import copy as copy # lets us clone objects without binding
import math

'''
LIST OF FEATURES:

menubar:
- mouse: click, hold, press, release, moveto (x,y), moveby (+- x, +- y)
- keys: click, hold, press, release, type (a whole string)
- other: sleep, start (wait for event), goto (repeat), speed (commands/second)

- setinterval changes background color of list items?

gui:
- insert command at certain location if an item in listbox is selected
- allow for saving/importing files
- make a command log (shows what you deleted/copied/added/edited/etc.)

command page metrics:
- mouse position
- currently pressing

logic:
- interval between commands
- repeating commands
'''
class Command:
    def __init__(self, name, vals):
        self.name = str(name)
        self.vals = vals #values to use to run
        self.isactive = False

    def save(self, vals):
        self.vals = vals
    
    def label(self):
        return self.name + ", " + str(self.vals)
'''
CLICK
name = "Click"
vals[0] = string (1 character) to click
vals[1] = (int) how many times to click
'''
class Click(Command):
    def __init__(self):
        Command.__init__(self, "Click", ["a", 1])
        self.controller = keyboard.Controller()

    def label(self):
        return "Click [" + self.vals[0] + "] " + str(self.vals[1]) + " times"

    def save(self, vals): #returns true if successful, false otherwise
        key = vals[0].get()
        repeat = vals[1].get()
        if repeat.isdigit() and len(key) == 1:
            self.vals = [key, int(repeat)]
            return True
        else:
            return False

    def run(self, keydict):
        for i in range(0, self.vals[1]):
            self.controller.tap(keydict[self.vals[0]])

'''
HOLD
name = "Hold"
vals[0] = string (1 character) to hold
vals[1] = how long (sec) to hold it
'''
class Hold(Command):
    def __init__(self):
        Command.__init__(self, "Hold", ["a", 1])
        self.controller = keyboard.Controller()

    def label(self):
        return "Hold [" + self.vals[0] + "] for " + str(self.vals[1]) + " seconds"

    def save(self, vals): #returns true if successful, false otherwise
        key = vals[0].get()
        time = vals[1].get()

        self.vals = [key, time]
        return True

    def run(self, keydict):
        self.controller.press(keydict[self.vals[0]])
        t.sleep(self.vals[1])
        self.controller.release(keydict[self.vals[0]])
'''
PRESS 
name = "Press"
vals[0] = string (1 character) to press
'''
class Press(Command):
    def __init__(self):
        Command.__init__(self, "Press", ["a"])
        self.controller = keyboard.Controller()

    def label(self):
        return "Press [" + self.vals[0] + "]"

    def save(self, vals):
        key = vals[0].get()

        self.vals = [key]
        return True

    def run(self, keydict):
        self.controller.press(keydict[self.vals[0]])
'''
RELEASE 
name = "Release"
vals[0] = string (1 character) to release
'''
class Release(Command):
    def __init__(self):
        Command.__init__(self, "Release", ["a"])
        self.controller = keyboard.Controller()

    def label(self):
        return "Release [" + self.vals[0] + "]"

    def save(self, vals):
        key = vals[0].get()

        self.vals = [key]
        return True

    def run(self, keydict):
        self.controller.release(keydict[self.vals[0]])
'''
TYPE
name = "Type"
vals[0] = string (1+ character) to type
'''
class Type(Command):
    def __init__(self):
        Command.__init__(self, "Type", ["abc"])
        self.controller = keyboard.Controller()

    def label(self):
        return "Type " + self.vals[0]

    def save(self, vals):
        string = vals[0].get()

        self.vals = [string]
        return True

    def run(self, keydict):
        self.controller.type(self.vals[0])
'''
MOVE MOUSE
name = "Move Mouse"
vals[0] = x coord to move to (0 <= x <= width)
vals[1] = y coord to move to (0 <= y <= height)
'''
class MoveMouse(Command):
    def __init__(self):
        Command.__init__(self, "Move Mouse", [0, 0])

        self.mousepos = (0, 0)

        self.controller = mouse.Controller()
        mouse.Listener(on_move=self.updatepos).start() #for curr pos

    def label(self):
        return "Move mouse to (" + str(self.vals[0]) + ", " + str(self.vals[1]) + ")"

    def save(self, vals):
        x = vals[0].get()
        y = vals[1].get()

        self.vals = [x, y]
        return True

    def updatepos(self, x, y):
        self.mousepos = (int(x), int(y))

    def run(self, keydict):
        dx = self.vals[0] - self.mousepos[0]
        dy = self.vals[1] - self.mousepos[1]

        self.controller.move(dx=dx, dy=dy)
        
'''
SCROLL MOUSE (equivalent to 2-finger movement on touchpad)
vals[0] = amount of steps (int)
vals[1] = direction (up, right, down, leeft)
'''
class Scroll(Command):
    def __init__(self):
        Command.__init__(self, "Scroll Mouse", [1, "down"])
        self.controller = mouse.Controller()

    def label(self):
        step = self.vals[0]
        direction = self.vals[1]

        return "Scroll mouse " + str(step) + " steps " + direction

    def save(self, vals):
        steps = vals[0].get()
        direction = vals[1].get()

        self.vals = [int(steps), direction]
        return True

    def run(self, keydict):
        '''
        scroll(dx, dy)

        negative <--- dx ----> positive

                positive
                    ^
                    |
                    |
                    dy
                    |
                    |
                    v
                negative
        '''
        s = self.vals[0]
        d = self.vals[1]

        if d == "up":
            self.controller.scroll(0, s)
        elif d == "down":
            self.controller.scroll(0, -s)
        elif d == "right":
            self.controller.scroll(s, 0)
        elif d == "left":
            self.controller.scroll(-s, 0)

'''
SLEEP
vals[0] = sec to sleep
'''
class Sleep(Command):
    def __init__(self):
        Command.__init__(self, "Sleep", [1])

    def label(self):
        return "Sleep " + str(self.vals[0]) + " seconds"

    def save(self, vals):
        sec = vals[0].get()

        self.vals = [int(sec)]
        return True

    def run(self, keydict):
        t.sleep(self.vals[0])

class Macro:
    def __init__(self):
        self.commands = [] #list of commands to execute
        self.curr = None #keep track of the index of our current stock
        self.title = "Macro Editor" #name of application
        self.wait = 0.5 #seconds in-between each command
        self.vals = [] #this will transfer gui info to commands

        self.root = tk.Tk() # Create a window
        self.root.title(self.title) # Set title
        self.root.geometry("800x800+200+50")
        self.root.resizable(width=False, height=False)

        #set up grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.notebook = Notebook(self.root, height=700)
        self.notebook.grid(sticky="NESW")

        #make the frames for the tab container
        self.commands_tab()
        self.manage_tab()
        self.history_tab()

        self.menu()

        #first use dictionary comprehension to add the alphanumerics + symbols
        no_shift = [39] + [x for x in range(44, 58)] + [59, 61, 91, 92, 93, 96] + [x for x in range(97, 123)] #see comment block in self.unshift()

        self.keydict = {chr(x):chr(x) for x in no_shift} # character name : character

        #now add the others
        self.keydict["space"] = " "
        self.keydict["bs"] = keyboard.Key.backspace
        self.keydict["caps"] = keyboard.Key.caps_lock
        self.keydict["cmd"] = keyboard.Key.cmd
        self.keydict["ctrl"] = keyboard.Key.ctrl
        self.keydict["enter"] = keyboard.Key.enter
        self.keydict["esc"] = keyboard.Key.esc
        self.keydict["shift"] = keyboard.Key.shift
        self.keydict["tab"] = keyboard.Key.tab
        self.keydict["lmb"] = mouse.Button.left
        self.keydict["rmb"] = mouse.Button.right
        self.keydict["mmb"] = mouse.Button.middle

        self.keys = [] #current keys pressed

        #alphanumeric button handler
        self.root.bind("<KeyPress>", self.handle_key_press)
        self.root.bind("<KeyRelease>", self.handle_key_release)

        #other buttons (key.char == "", so we use key.keysym to get key symbol)

        #press
        self.root.bind("<KeyPress-space>", lambda key : self.handle_other_key_press("space"))
        self.root.bind("<KeyPress-Meta_R>", lambda key : self.handle_other_key_press("cmd"))
        self.root.bind("<KeyPress-Meta_L>", lambda key : self.handle_other_key_press("cmd"))
        self.root.bind("<KeyPress-Meta_R>", lambda key : self.handle_other_key_press("cmd"))
        self.root.bind("<KeyPress-Control_L>", lambda key : self.handle_other_key_press("ctrl"))
        self.root.bind("<KeyPress-Control_R>", lambda key : self.handle_other_key_press("ctrl"))
        self.root.bind("<KeyPress-Shift_L>", lambda key : self.handle_other_key_press("shift"))
        self.root.bind("<KeyPress-Shift_R>", lambda key : self.handle_other_key_press("shift"))
        self.root.bind("<KeyPress-Tab>", lambda key : self.handle_other_key_press("tab"))
        self.root.bind("<KeyPress-Caps_Lock>", lambda key : self.handle_other_key_press("caps"))
        self.root.bind("<KeyPress-Escape>", lambda key : self.handle_other_key_press("esc"))
        self.root.bind("<KeyPress-Return>", lambda key : self.handle_other_key_press("enter"))
        self.root.bind("<KeyPress-BackSpace>", lambda key : self.handle_other_key_press("bs"))

        #release
        self.root.bind("<KeyRelease-space>", lambda key : self.handle_other_key_release("space"))
        self.root.bind("<KeyRelease-Meta_L>", lambda key : self.handle_other_key_release("cmd"))
        self.root.bind("<KeyRelease-Meta_R>", lambda key : self.handle_other_key_release("cmd"))
        self.root.bind("<KeyRelease-Control_L>", lambda key : self.handle_other_key_release("ctrl"))
        self.root.bind("<KeyRelease-Control_R>", lambda key : self.handle_other_key_release("ctrl"))
        self.root.bind("<KeyRelease-Shift_L>", lambda key : self.handle_other_key_release("shift"))
        self.root.bind("<KeyRelease-Shift_R>", lambda key : self.handle_other_key_release("shift"))
        self.root.bind("<KeyRelease-Tab>", lambda key : self.handle_other_key_release("tab"))
        self.root.bind("<KeyRelease-Caps_Lock>", lambda key : self.handle_other_key_release("caps"))
        self.root.bind("<KeyRelease-Escape>", lambda key : self.handle_other_key_release("esc"))
        self.root.bind("<KeyRelease-Return>", lambda key : self.handle_other_key_release("enter"))
        self.root.bind("<KeyRelease-BackSpace>", lambda key : self.handle_other_key_release("bs"))

        # for some reason, py freaks out when theres a mouse and key listener
        # so the keys are being handled with tkinter, the mouse is being handled with pynput
        mouse.Listener(on_move=self.update_mouse).start()

        self.root.mainloop()

    def unshift(self, key): #takes a key (shift/caps lock pressed) and finds its corresponding unshifted key, returns the key if its already unshifted 
        '''
        all the ascii codes for keys that can be pressed without using shift/caps lock
        39      '
        44-47   , - . /
        48-57   0 to 9
        59      ;
        61      =
        91-93   [ ] \
        96      `
        97-122  a to z
        
        all the ascii codes for keys that can be pressed with using shift OR capslock
        65-90   A to Z

        all the ascii codes for keys that can be pressed with using shift ONLY
        33-38   ! " $ % &
        40-43   ( ) * +
        58      :
        60      <
        62-64   > ? @
        65-90   A to Z
        94-95   ^ _
        123-126 { | } ~
        '''
        
        #yes this was done by hand
        #shifted value : unshifted value
        dict = \
            {33:49} | \
            {34:39} | \
            {35:51} | \
            {36:52} | \
            {37:53} | \
            {38:55} | \
            {40:57} | \
            {41:48} | \
            {42:56} | \
            {43:61} | \
            {58:59} | \
            {60:44} | \
            {62:46} | \
            {63:47} | \
            {64:50} | \
            {94:54} | \
            {95:45} | \
            {123:91} | \
            {124:92} | \
            {125:93} | \
            {126:96}

        key = ord(key)
        rtn = key

        if "shift" in self.keys: #shift/caps lock pressed
            if 65 <= key and key <= 90: #A-Z
                rtn = key + 32
            else:
                rtn = dict[key]
        elif "caps" in self.keys: #caps lock pressed
            rtn = key + 32 #a-z <-- A-Z

        return chr(rtn)

    def commands_tab(self):
        tab = Frame(self.notebook)
        tab.grid()

        #set up grid
        tab.rowconfigure(0, weight=1)
        tab.rowconfigure(1, weight=1)
        tab.rowconfigure(2, weight=2)
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=2)

        #listbox
        self.list = tk.Listbox(tab, selectmode=tk.EXTENDED)
        self.list.grid(row=0, rowspan=3, column=0, sticky="NSEW", padx=5, pady=5)
        self.list.bind("<<ListboxSelect>>", self.listbox_select)

        mouseframe = LabelFrame(tab, text="Mouse")
        mouseframe.grid(row=0, column=1, sticky='NESW', padx=5, pady=5)

        mouseframe.rowconfigure(0, weight=1)
        mouseframe.columnconfigure(0, weight=1)

        #dynamic text label
        self.mousevar = tk.StringVar()
        self.mousevar.set("Mouse Position:")

        mouselabel = Label(mouseframe, textvariable=self.mousevar, width=25)
        mouselabel.grid(sticky="NSW")

        keyframe = LabelFrame(tab, text="Keyboard")
        keyframe.grid(row=1, column=1, sticky="NESW")

        keyframe.rowconfigure(0, weight=1)
        keyframe.columnconfigure(0, weight=1)

        #dynamic text label
        self.keyvar = tk.StringVar()
        self.keyvar.set("Keys Pressed: ")

        keylabel = Label(keyframe, textvariable=self.keyvar, width=25)
        keylabel.grid(sticky="NSW")

        self.notebook.add(tab, text="Commands")

    def handle_key_press(self, key):
        self.keys.append(self.unshift(key.char))
        self.update_key()

    def handle_key_release(self, key):
        self.keys.remove(self.unshift(key.char))
        self.update_key()

    def handle_other_key_press(self, key):
        self.keys.append(key)
        self.update_key()

    def handle_other_key_release(self, key):
        self.keys.remove(key)
        self.update_key()

    def update_key(self):
        strkeys = ""

        #format the things to be pressed
        for i in range(0, len(self.keys)):
            strkeys += self.keys[i]
            if i < len(self.keys) - 1: #dont add this on the last one or it looks weird
                strkeys += "+"

        self.keyvar.set("Keys Pressed: " + strkeys)

    def update_mouse(self, x, y):
        mousepos = (int(x), int(y))
        self.mousevar.set("Mouse Position: " + str(mousepos))

    def manage_tab(self):
        self.manage = Frame(self.notebook)
        self.manage.grid()
        self.notebook.add(self.manage, text="Manage")

        #set up grid
        self.manage.rowconfigure(0, weight=1)
        self.manage.rowconfigure(1, weight=1)
        self.manage.rowconfigure(2, weight=9)
        self.manage.columnconfigure(0, weight=1)

        self.load_managedefault()

    def history_tab(self):
        tab = Frame(self.notebook)
        tab.grid()
        self.notebook.add(tab, text="History")

        #set up grid
        tab.rowconfigure(0, weight=1)

        #text box
        self.historylog = tk.Text(tab)
        self.historylog.grid(row=0, sticky="NS")

    def menu(self):
        #make a menu bar widget (container for the cascade menus at the top of the window)
        menubar = tk.Menu(self.root) #container is the root window

        #configure the root with the menu bar
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0) #tearoff does not let you move the menu out of the window
        file_menu.add_command(label="Run", command=self.run)
        file_menu.add_command(label="Stop", command=self.stop)
        file_menu.add_separator()
        file_menu.add_command(label="Import CSV...")
        file_menu.add_command(label="Export to CSV...")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=quit)

        edit_menu = tk.Menu(menubar, tearoff=0) #tearoff does not let you move the menu out of the window
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Delete", command=self.delete)

        add_menu = tk.Menu(menubar, tearoff=0) #tearoff does not let you move the menu out of the window
        add_menu.add_command(label="Click", command=self.click)
        add_menu.add_command(label="Hold", command=self.hold)
        add_menu.add_command(label="Press", command=self.press)
        add_menu.add_command(label="Release", command=self.release)
        add_menu.add_command(label="Type", command=self.type)
        add_menu.add_separator()
        add_menu.add_command(label="Move Mouse", command=self.movemouse)
        add_menu.add_command(label="Scroll Mouse", command=self.scroll)
        add_menu.add_separator()
        add_menu.add_command(label="Sleep", command=self.sleep)


        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        menubar.add_cascade(label="Commands", menu=add_menu)

    def load_managesave(self, frame): #adds two buttons to the bottom of a command manage labelframe

        #now do the buttons
        delbutton = Button(frame, command=self.delete, text="Delete")
        delbutton.grid(row=2, column=0, sticky="NS")

        savebutton = Button(frame, command=self.save, text="Save")
        savebutton.grid(row=2, column=1, sticky="NS")

    def load_managedefault(self):
        #the default frame when no command(s) is selected
        frame = Frame(self.manage)
        frame.grid(row=0, column=0)
        
        none = Label(frame, text="No Command Selected")
        none.grid()

    def listbox_select(self, event): #handles a new stock being selected in listbox
        curr = self.list.curselection() #returns a tuple
        if self.notebook.index(self.notebook.select()) == 0: #only allow changes if on the comamnds tab
            if curr == (): #when something is deselected, its an empty tuple
                index = None #just reselect whatever was previously selected
            else:
                index = curr[0] #since the listbox only allows single selection, the tuple only has 1 item
            self.load_curr(index)

    def run(self):
        for i in range(0, len(self.commands)):
            self.commands[i].run(self.keydict)
            t.sleep(self.wait)

    def stop(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def cut(self):
        pass

    def delete(self):
        if self.curr != None:
            self.list.delete(self.curr)
            self.load_curr(None)

    def click(self):
        cmd = Click()
        self.listbox_add(cmd)
    
    def load_click(self):
        frame = LabelFrame(self.manage, text="Click")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        key1 = Label(frame, text="Click ")
        key1.grid(row=0, column=0)

        val0 = tk.StringVar()
        val0.set(self.commands[self.curr].vals[0]) # put default val
        self.vals.append(val0)

        key2 = Combobox(frame, textvariable=self.vals[0])

        key2values = list(self.keydict.keys()) #all the labels
        key2["values"] = key2values

        key2.state(["readonly"])

        key2.grid(row=0, column=1)

        #vals[1]
        val1 = tk.StringVar()
        val1.set(self.commands[self.curr].vals[1])
        self.vals.append(val1)

        repeat1 = Label(frame, text="Repeat ")
        repeat1.grid(row=1, column=0)
        repeat2 = Spinbox(frame, from_=1, to=100, textvariable=self.vals[1])
        repeat2.grid(row=1, column=1)
        repeat3 = Label(frame, text=" times.")
        repeat3.grid(row=1, column=2)

        self.load_managesave(frame)

    def hold(self):
        cmd = Hold()
        self.listbox_add(cmd)

    def load_hold(self):
        frame = LabelFrame(self.manage, text="Hold")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        key1 = Label(frame, text="Hold ")
        key1.grid(row=0, column=0)

        val0 = tk.StringVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        key2 = Combobox(frame, textvariable=self.vals[0])

        key2values = list(self.keydict.keys()) #all the labels
        key2["values"] = key2values

        key2.state(["readonly"])

        key2.grid(row=0, column=1)

        #vals[1]
        val1 = tk.IntVar()
        val1.set(self.commands[self.curr].vals[1])
        self.vals.append(val1)

        repeat1 = Label(frame, text="Hold for ")
        repeat1.grid(row=1, column=0)
        repeat2 = Spinbox(frame, from_=1, to=100, textvariable=self.vals[1])
        repeat2.grid(row=1, column=1)
        repeat3 = Label(frame, text=" seconds.")
        repeat3.grid(row=1, column=2)

        self.load_managesave(frame)

    def press(self):
        cmd = Press()
        self.listbox_add(cmd)

    def load_press(self):
        frame = LabelFrame(self.manage, text="Press")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        key1 = Label(frame, text="Press ")
        key1.grid(row=0, column=0)

        val0 = tk.StringVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        key2 = Combobox(frame, textvariable=self.vals[0])

        key2values = list(self.keydict.keys()) #all the labels
        key2["values"] = key2values

        key2.state(["readonly"])

        key2.grid(row=0, column=1)

        self.load_managesave(frame)

    def release(self):
        cmd = Release()
        self.listbox_add(cmd)

    def load_release(self):
        frame = LabelFrame(self.manage, text="Release")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        key1 = Label(frame, text="Release ")
        key1.grid(row=0, column=0)

        val0 = tk.StringVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        key2 = Combobox(frame, textvariable=self.vals[0])

        key2values = list(self.keydict.keys()) #all the labels
        key2["values"] = key2values

        key2.state(["readonly"])

        key2.grid(row=0, column=1)

        self.load_managesave(frame)

    def type(self):
        cmd = Type()
        self.listbox_add(cmd)

    def load_type(self):
        frame = LabelFrame(self.manage, text="Type")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        key1 = Label(frame, text="Type ")
        key1.grid(row=0, column=0)

        val0 = tk.StringVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        key2 = Entry(frame, textvariable=self.vals[0])
        key2.grid(row=0, column=1)

        self.load_managesave(frame)

    def movemouse(self):
        cmd = MoveMouse()
        self.listbox_add(cmd)
    
    def load_movemouse(self):
        frame = LabelFrame(self.manage, text="Move Mouse")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        x1 = Label(frame, text="Move mouse x to ")
        x1.grid(row=0, column=0)

        val0 = tk.IntVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        x2 = Spinbox(frame, textvariable=self.vals[0], from_=0, to=self.root.winfo_screenwidth()) #0-width of screen
        x2.grid(row=0, column=1)

        #vals[1]
        y1 = Label(frame, text="Move mouse y to ")
        y1.grid(row=1, column=0)

        val1 = tk.IntVar()
        val1.set(self.commands[self.curr].vals[1])
        self.vals.append(val1)

        y2 = Spinbox(frame, textvariable=self.vals[1], from_=1, to=self.root.winfo_screenheight())
        y2.grid(row=1, column=1)

        self.load_managesave(frame)

    def scroll(self):
        cmd = Scroll()
        self.listbox_add(cmd)

    def load_scroll(self):
        frame = LabelFrame(self.manage, text="Scroll Mouse")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        step1 = Label(frame, text="Scroll ")
        step1.grid(row=0, column=0)

        val0 = tk.IntVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        step2 = Spinbox(frame, textvariable=self.vals[0], from_=1, to=100)

        step2.grid(row=0, column=1)
        
        step3 = Label(frame, text=" steps.")
        step3.grid(row=0, column=2)

        #vals[1]
        val1 = tk.StringVar()
        val1.set(self.commands[self.curr].vals[1])
        self.vals.append(val1)

        d1 = Label(frame, text="Scroll in ")
        d1.grid(row=1, column=0)

        d2 = Combobox(frame, textvariable=self.vals[1])
        d2["values"] = ["up", "down", "right", "left"]
        d2.state(["readonly"])
        d2.grid(row=1, column=1)

        d3 = Label(frame, text=" direction.")
        d3.grid(row=1, column=2)

        self.load_managesave(frame)

    def sleep(self):
        cmd = Sleep()
        self.listbox_add(cmd)
    
    def load_sleep(self):
        frame = LabelFrame(self.manage, text="Sleep")
        frame.grid(row=0, column=0)

        #set up grid, 2 x 3
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #vals[0]
        step1 = Label(frame, text="Sleep for ")
        step1.grid(row=0, column=0)

        val0 = tk.IntVar()
        val0.set(self.commands[self.curr].vals[0])
        self.vals.append(val0)

        step2 = Spinbox(frame, textvariable=self.vals[0], from_=1, to=100)

        step2.grid(row=0, column=1)
        
        step3 = Label(frame, text=" seconds.")
        step3.grid(row=0, column=2)

        self.load_managesave(frame)

    def listbox_add(self, x):
        self.list.insert(len(self.commands), x.label())
        self.commands.append(x)

    def load_curr(self, i):
        self.curr = i

        #delete current manage tab children
        for i in self.manage.winfo_children():
            i.destroy()

        #reset vals
        self.vals = []

        if self.curr != None:
            #load the new one
            if self.commands[self.curr].name == "Click":
                self.load_click()
            if self.commands[self.curr].name == "Hold":
                self.load_hold()
            if self.commands[self.curr].name == "Press":
                self.load_press()
            if self.commands[self.curr].name == "Release":
                self.load_release()
            if self.commands[self.curr].name == "Type":
                self.load_type()
            if self.commands[self.curr].name == "Move Mouse":
                self.load_movemouse()
            if self.commands[self.curr].name == "Scroll Mouse":
                self.load_scroll()
            if self.commands[self.curr].name == "Sleep":
                self.load_sleep()
        else:
            self.load_managedefault()

    def save(self):
        cmd = self.commands[self.curr]

        #save changes
        cmd.save(self.vals)
        
        #update label
        self.list.delete(self.curr)
        self.list.insert(self.curr, cmd.label())





Macro() #make a new object to start the GUI