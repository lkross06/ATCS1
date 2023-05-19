#Lucas Ross 21 Oct. 2022
from tkinter import *
import random as r
from math import fabs

class Ball:
    def __init__(self, canvas, width):
        self.x = r.randint(0, width) # Starting center position
        self.y = 0 
        self.dx = r.randint(0, 10) - 5 # randomly move left or right
        self.dy = r.randint(1, 9) # move down at a random speed
        self.radius = 40 # The radius is fixed
        self.color = self.randomcolor() # Get random color

        #add the node to the canvas (self.node is the ID of the object)
        self.node = canvas.create_oval(self.x, self.y, self.x + self.radius, self.y + self.radius, outline = "#000000", fill = "#" + self.color)

    # Return a random color string in the form #RRGGBB
    def randomcolor(self):
        num = r.randint(0, 16777215)
        num = hex(num)
        while len(num[2:]) < 6:
            num = num + "0"
        return num[2:]

class GameLogic:
    def __init__(self, width, height):
        self.score = 0
        self.balls = []
        self.sleep = 40 # amount of ms in between frames

        #dimensions of canvas
        self.width = width
        self.height = height

    def move(self, ball):

        #otherwise just move it
        self.bouncex(ball)

        ball.x += ball.dx
        ball.y += ball.dy
    
    def bouncex(self, ball): #Checks if the oval should bounce, bounces if necessary
        # right wall
        if ball.x + ball.radius >= self.width:
            ball.dx = -fabs(ball.dx)

        # left wall
        if ball.x <= 0:
            ball.dx = fabs(ball.dx)


class GameGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Ball Pop Game")

        #dimensions of canvas
        self.width = 500
        self.height = 500

        self.logic = GameLogic(self.width, self.height)

        #container for score
        self.frame = Frame(self.root)
        self.frame.pack()

        self.scorelabel = Label(self.frame, text="Score: ")
        self.scorelabel.pack(side=LEFT)

        self.score = Label(self.frame, text="")
        self.score.pack(side=LEFT)

        #draw everything on it
        self.canvas = Canvas(self.root, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        #event listener
        #<Button-1> is left mouse button (right mouse button on laptop)
        self.canvas.bind("<Button-1>", self.click)

        self.update()

        self.root.mainloop()
    
    def click(self, event):
        x = event.x
        y = event.y
        for ball in self.logic.balls:
            #check if click was within any balls
            '''
            (x - h)^2 + (y - k)^2 < r^2

            x   x coord of mouse
            y   y coord of mouse
            h   x coord of ball center
            k   y coord of ball center
            r   radius of ball
            '''
            if (x - ball.x)**2 + (y - ball.y)**2 <= ball.radius**2:
                self.delete_ball(ball)
                self.logic.score += 1
    
    def delete_ball(self, ball):
        self.canvas.delete(ball.node)
        self.logic.balls.remove(ball)

    def add_ball(self):
        self.logic.balls.append(Ball(self.canvas, self.width))

    def update(self): #updates the animation
        #randomly spawn new balls
        rand = r.randint(0, 30)
        if rand == 0:
            self.add_ball()

        self.move() #move all the balls

        self.score.config(text=str(self.logic.score)) #update score label

        #repeat after logic.sleep ms
        self.canvas.after(self.logic.sleep, self.update)

    def move(self):
        for ball in self.logic.balls:
            # check if its off the screen (bottom wall)
            if ball.y > self.height:
                self.delete_ball(ball)

            self.logic.move(ball)
            self.canvas.move(ball.node, ball.dx, ball.dy)

#initialize game window
gui = GameGUI()

