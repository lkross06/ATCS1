import tkinter as tk

root = tk.Tk()
root.geometry("500x500+100+100")
root.title("Arithmatic GUI")

#number 1
num1l = tk.Label(root, text="Number 1: ")
num1l.grid(row=1, column=1)

num1e = tk.Entry(root)
num1e.grid(row=1, column=2)

#number 2
num2l = tk.Label(root, text="Number 2: ")
num2l.grid(row=2, column=1)

num2e = tk.Entry(root)
num2e.grid(row=2, column=2)

#arithmatic functions
def add():
    try:
        num1 = float(num1e.get())
        num2 = float(num2e.get())
        resl.set(str(format(num1 + num2, ".2f")))
    except ValueError:
        resl.set("Invalid Input!")
def sub():
    try:
        num1 = float(num1e.get())
        num2 = float(num2e.get())
        resl.set(str(format(num1 - num2, ".2f")))
    except ValueError:
        resl.set("Invalid Input!")
def mul():
    try:
        num1 = float(num1e.get())
        num2 = float(num2e.get())
        resl.set(str(format(num1 * num2, ".2f")))
    except ValueError:
        resl.set("Invalid Input!")
def div():
    try:
        num1 = float(num1e.get())
        num2 = float(num2e.get())
        resl.set(str(format(num1 / num2, ".2f")))
    except ValueError:
        resl.set("Invalid Input!")

#result
resl = tk.StringVar()
res = tk.Label(root, textvariable=resl)
res.grid(row=3, column=1)

#arithmatic buttons
addb = tk.Button(root, text="Add", command=add)
addb.grid(row=4, column=1)
subb = tk.Button(root, text="Subtract", command=sub)
subb.grid(row=4, column=2)
mulb = tk.Button(root, text="Multiply", command=mul)
mulb.grid(row=4, column=3)
divb = tk.Button(root, text="Divide", command=div)
divb.grid(row=4, column=4)

#arithmatic menu

#first make a menubar and config to root
menu = tk.Menu(root)
root.config(menu=menu)

#now make the operation cascade
op = tk.Menu(menu, tearoff=0)
op.add_command(label="Add", command=add)
op.add_command(label="Subtract", command=sub)
op.add_command(label="Multiply", command=mul)
op.add_command(label="Divide", command=div)

menu.add_cascade(label="Operation", menu=op)

#exit cascade
ex = tk.Menu(menu, tearoff=0)

destroy = ex.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="Exit", menu=ex)
 
root.mainloop()