import turtle as t
import random as r

'''
makes a grid backdrop

size: how many spaces per row and column
pad: padding in between lines
w: width of line
'''
def makeGrid(size, pad, w):
    tl = [-((size *  pad) / 2) - ((size / 2) * w), ((size *  pad) / 2) + ((size / 2) * w)] #x and y coords for topleft of grid

    #change pen settings
    t.color("black")
    t.width(w)
    t.mode("standard") #for some reason this puts the pen down, so put the pen up immediately after
    t.penup()
    t.speed(10)

    #now go to top left corner and draw vertical lines
    t.goto(tl[0], tl[1])
    t.setheading(270) #make it face south
    i = 1 #keep track of each iteration for positioning
    
    while t.xcor() <= ((size *  pad) / 2) + ((size / 2) * w):
        t.pendown()
        t.forward((size * pad) + (size * w))
        t.penup()
        t.goto(tl[0] + ((pad + w) * i), tl[1])
        i += 1

    #now go to top left corner and draw horizontal lines
    t.goto(tl[0], tl[1])
    t.setheading(0)
    i = 1 #keep track of each iteration for positioning
    
    while t.ycor() >= -((size *  pad) / 2) - ((size / 2) * w):
        t.pendown()
        t.forward((size * pad) + (size * w))
        t.penup()
        t.goto(tl[0], tl[1] - ((pad + w) * i))
        i += 1
    t.goto(0, 0)
    
'''
randomly finds a path out of a grid given that the pen starts in the middle

size: size of grid (see above)
pad: padding in between each line of grid
w: width of grid lines
'''
def pathfindOut(size, pad, w):
    #keep track of x and y displacement (from the center of the grid) so we know when you have exited the grid completely
    dx = 0
    dy = 0

    #pen settings
    
    t.width(10)
    t.color("red", "black")
    t.speed(1)
    t.penup()
    
    #start in the middle of the grid
    t.goto(w, w)
    t.pendown()

    exited = False
    while not(exited):

        '''
        0 : east
        90 : north
        180 : west
        270 : south
        '''
        choices = [0, 90, 180, 270]
        rand_turn = r.randint(0, 3) #each "turn", make a random direction change
        deg = choices[rand_turn]
        t.setheading(deg)
        t.forward(pad + w)

        if deg == 0:
            dx += 1
        if deg == 90:
            dy += 1
        if deg == 180:
            dx -= 1
        if deg == 270:
            dy -= 1
        
        #check if they are outside of the grid yet
        if abs(dx) >= (size / 2) or abs(dy) >= (size / 2):
            exited = True
    
pad = 50
w = 1
numspaces = 8 #better with even number of spaces
makeGrid(numspaces, pad, w)
pathfindOut(numspaces, pad, w)
t.done()


