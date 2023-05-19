'''
menu bar is the drop-down menu in the top-left of applications
(i.e. File->Open, Close, Exit)

it is programmable to do specific things to the program with tkinter!
'''
import tkinter as tk

#set up root window
main_window = tk.Tk()
main_window.title("Menu Window")
main_window.geometry("300x400")

#make a menu bar widget
menubar = tk.Menu(main_window) #container is the root window

#configure the window with the menu bar
main_window.config(menu=menubar)

#add commands (buttons that run a function when u click it)
file_menu = tk.Menu(menubar, tearoff=0) #container is the menubar obj
#tearoff does not let you move the menu out of the window
file_menu.add_command(label="Open")
file_menu.add_command(label="Close")
file_menu.add_command(label="Exit", command=main_window.destroy) #root.destroy() closes itself

#add the cascade (menu group) to the container with the cascade name
menubar.add_cascade(label="File", menu=file_menu)

main_window.mainloop()