#imports everything from the module
import tkinter as tk

#use the function with the button
def calculatekm():
    try:
        mi = float(e1.get()) #get the input in the entry object
        km = mi*1.6
        input.set(str(km)) #set the label text to this
    except ValueError:
        input.set("Invalid Input!")

#create new root window
main_window = tk.Tk()
main_window.geometry("300x400")

#create label
l1 = tk.Label(main_window, text="Enter distance in miles: ", padx=5, pady=5) #padx and pady = padding in the grid cell
l1.grid(row=1, column=1)

#create text box
e1 = tk.Entry(main_window)
e1.grid(row=1, column=2) #position to the right of the label

#create another label with a dynamic text
input = tk.StringVar()
l2 = tk.Label(main_window, textvariable=input) #text variable -> string (special tkinter class) to display
l2.grid(row=2, column=1)

#create a button
#when the user clicks on the button, calculate the km and display
b1 = tk.Button(main_window, text="Calculate", command=calculatekm)
b1.grid(row=3, column=1)

main_window.mainloop() #make it not close