import turtle as t
import random as r

class point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

'''
gets the midpoint of two points and returns it as a new point

p1  first point
p2  second point
'''
def midpoint(p1, p2):
    x = (p1.x + p2.x) / 2
    y = (p1.y + p2.y) / 2
    return point(x, y)

'''
adds a point to the GUI with turtle

p   point to add
'''
def addpoint(p):
    t.penup()
    t.goto(p.x, p.y)
    t.pendown()
    t.dot()
    t.penup()

def pick2random(arr):
    #pick one of the three original points
    i1 = r.randint(0, 2)
    #pick any other point that isnt the first
    while True:
        i2 = r.randint(0, len(arr) - 1)
        if i1 != i2:
            break
    return [arr[i1], arr[i2]]
    
size = 400
iterations = 8000

t.penup()
t.goto(0, 0)
t.speed(10)

r.seed(9)

#add the vertices to the triangle
t.color("red")
v1 = point(0, size - (size/2))
v2 = point(-(size/2), 0 - (size/2))
v3 = point((size/2), 0 - (size/2))
pts = [v1, v2, v3]
addpoint(v1)
addpoint(v2)
addpoint(v3)
t.color("black")

for i in range(1, iterations):
    rand = pick2random(pts)
    new = midpoint(rand[0], rand[1])
    pts.append(new)
    addpoint(new)

t.done()