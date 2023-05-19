from tkinter import *
import tkinter.messagebox

'''
handles logic of binary search
'''
class StepControl:
    def __init__(self):
        self.num_items = 20
        self.list = [ x for x in range(1, self.num_items + 1) ]
        self.key = 0

        self.reset()

    def reset(self):
        #these represent indices
        self.low = 0
        self.high = len(self.list) - 1
        self.mid = -1 #if its -1, then dont draw anything

        self.done = False
        self.iterations = 0
        self.initial_key = self.key #if these two ever differ, the user changed key in-between steps

        self.drawAStep()

    def step(self):
        if self.initial_key == self.key:
            #perform one iteration of the algorithm

            if self.key == self.mid: #we found the index in the array
                self.high = self.key
                self.low = self.key
                self.done = True
            elif self.key > self.mid: #right side
                self.low = self.mid + 1
            else: #left side             
                self.high = self.mid - 1

            #get the new mid
            self.mid = int((self.low + self.high) / 2) # round to int (bc its an index)
            
            #finally redraw it
            self.drawAStep()

            #increment iterations
            if not(self.done):
                self.iterations += 1
        else:
            #restart the algorithm, then call itself
            self.reset()
            self.step()

    def drawABar(self, i, w, h, o, f):
        #width of each bar
        bwidth = w / self.num_items
        #height of each bar (considering 1 "unit")
        bheight = h / (self.num_items + 2) #1 for i=0, 1 for label at i=19
        #x coord (top-left)
        x = bwidth * i
        #y coord (top-left)
        y = h - ((i + 1) * bheight)

        canvas.create_rectangle(x, y, x + bwidth, h, outline=o, fill=f)
        canvas.create_text(x + 7, y - 6, text=str(i + 1), font=('Arial',str(int(bwidth) - 4)))

    def drawAStep(self):
        #erase current canvas
        canvas.delete("all")   

        #get colors
        colors = []
        if self.mid == -1: # reset
            colors = ["white" for x in range(0, len(self.list))]
        else:
            for i in range(0, len(self.list)):
                if i <= self.high and i >= self.low:
                    if i == self.mid:
                        colors.append("red")
                    else:
                        colors.append("gray")
                else:
                    colors.append("white")

        #draw the bars
        for i in range(0, len(self.list)):
            self.drawABar(i, width, height, "black", colors[i])
        
        #show message box if its done
        if self.done:
            tkinter.messagebox.showinfo(title="Item Found", message="Item " + str(int(self.key) + 1) + " has been found in " + str(self.iterations) + " iterations.")



def step():
    input = key.get()
    try:
        temp = int(input) - 1 # - 1 because its an index
        #if its outside bounds, throw an error so it doesnt procede
        if temp <= len(control.list) and temp >= 0:
            control.key = temp
            control.step()
        else:
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror(title="Invalid Input", message="Invalid input for binary search key.")


def reset():
    control.reset()
    
window = Tk() # Create a window
window.title("Binary Search Animation") # Set title

width = 340
height = 150
radius = 2
canvas = Canvas(master=window, width=width, height=height)
canvas.pack()

frame = Frame(window)
frame.pack()

control = StepControl()

Label(frame, text = "Enter a key:").pack(side = LEFT)
key = StringVar()
Entry(frame, textvariable = key, justify = RIGHT, width = 3).pack(side = LEFT)
Button(frame, text = "Step", command = step).pack(side = LEFT)
Button(frame, text = "Reset", command = reset).pack(side = LEFT)


window.mainloop() # Create an event loop
