import tkinter as tk

class GUI:
    def __init__(self):
        #root window
        self.root = tk.Tk()
        self.root.geometry("600x600+100+100") #width, height, x, y
        self.root.title("intro to tkinter")

        self.l1 = self.makelabel(self.root)
        self.b1 = self.makebutton(self.root)

        #finally, show the window
        self.root.mainloop()

    #label
    def makelabel(self, root):
        l = tk.Label(root, text="YAYA")
        l.grid(row=1, column=1)
        return l

    #button
    def makebutton(self, root):
        '''
        args:
        text        text inside button
        command     functional object to run on button click
        '''
        #USE \ TO PUT THE SAME COMMAND ON A DIFFERENT LINE OF THE DOCUMENT!!!!
        b = tk.Button(root, text="YAYA",\
             command=self.buttonaction)
        b.grid(row=2, column=1)
        return b
    
    def buttonaction(self):
        print("WOOO")
        
gui = GUI()