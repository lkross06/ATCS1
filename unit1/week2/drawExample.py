from time import sleep
import turtle as t
import random as r
#t and r are name of objects from turtle and random classes

#change speed of object
t.speed(900)
#go forward 100px
t.forward(100)
#90 degree angle to the right
t.right(90)
t.forward(50)
#change color of drawing line and object to blue (idk what green does)
t.color("blue", "green")
i = 0
while i < 100:
    #start the line drawing
    t.begin_fill
    #go to coordinates on window
    t.goto(0, 0)
    t.forward(r.randint(0, 100))
    t.right(r.randint(50, 100))
    t.forward(r.randint(50, 500))
    t.left(r.randint(50, 125))
    i += 1
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
#do nothing for 5 seconds
sleep(5)

#then tell turtle to stop
t.done()