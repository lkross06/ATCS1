from tkinter import * # Import tkinter
from random import randint
from math import fabs

# Return a random color string in the form #RRGGBB
def getRandomColor():
    num = randint(0, 16777215)
    num = hex(num)
    while len(num[2:]) < 6:
        num = num + "0"
    return num[2:]
        
# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 8 # The radius is fixed
        self.color = getRandomColor() # Get random color

class BounceBalls:
    def __init__(self):
        self.ballList = [] # Create a list for Ball object
        self.ovalList = [] # Create a list for create_oval objects
        
        self.window = Tk() # Create a window
        self.window.title("Bouncing Balls") # Set a title
        
        self.width = 350 # Width of the self.canvas
        self.height = 150 # Width of the self.canvas
        self.canvas = Canvas(self.window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(self.window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
            command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        
        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        self.animate()
        
        self.window.mainloop() # Create an event loop
           
    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False
    
    def add(self): # Add a new ball
        ball = Ball()
        oval = self.canvas.create_oval(ball.x, ball.y, ball.x + ball.radius, ball.y + ball.radius, outline = "#000000", fill = "#" + ball.color)

        self.ballList.append(ball)
        self.ovalList.append(oval)
    
    def remove(self): # Remove the last ball
        if self.ballList:
            self.ballList.pop()
            self.canvas.delete(self.ovalList.pop())
                                
    def animate(self): # Move the message
        if not(self.isStopped):
            for i in range(0, len(self.ballList)):
                ball = self.ballList[i]
                oval = self.ovalList[i]

                self.bounce(ball)

                ball.x += ball.dx
                ball.y += ball.dy
                
                self.canvas.move(oval, ball.dx, ball.dy)
        self.canvas.after(self.sleepTime, self.animate)
    
    def bounce(self, ball): #Checks if the oval should bounce, bounces if necessary
        # right wall
        if ball.x + ball.radius >= self.width:
            ball.dx = -fabs(ball.dx)

        # left wall
        if ball.x <= 0:
            ball.dx = fabs(ball.dx)

        # top wall
        if ball.y <= 0:
            ball.dy = fabs(ball.dy)

        # bottom wall
        if ball.y + ball.radius >= self.height:
            ball.dy = -fabs(ball.dy)
                                             
BounceBalls() # Create GUI
