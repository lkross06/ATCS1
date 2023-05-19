#distance formula
from math import dist

good_x = False
x = 0
#put a loop until a valid input is given
while not(good_x):
    tx = input("x: ")
    #positive or negative int
    if tx.isdigit() or (tx.startswith("-") and tx[1:].isdigit()):
        good_x = True
        x = int(tx)
    #invalid or float
    else:
        try:
            tx = float(tx)
            good_x = True
            x = float(tx)
        except ValueError:
            print("Incorrect input, try again.")
good_y = False
y = 0
#put a loop until a valid input is given
while not(good_y):
    ty = input("y: ")
    #positive or negative int
    if ty.isdigit() or (ty.startswith("-") and ty[1:].isdigit()):
        good_y = True
        y = int(ty)
    #invalid or float
    else:
        try:
            ty = float(ty)
            good_y = True
            y = float(ty)
        except ValueError:
            print("Incorrect input, try again.")

#split point (x,y) into intercepts (x,0) and (0,y) and test distance individually
dy = dist([0,0], [0,y])
dx = dist([0,0], [x,0])

if dy > 2.5 or dx > 5:
    print("(" + str(x) + ", " + str(y) + ") is not in the 10 x 5 rectangle at (0, 0)")
else:
    print("(" + str(x) + ", " + str(y) + ") is in the 10 x 5 rectangle at (0, 0)")