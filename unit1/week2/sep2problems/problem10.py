#since we have 8 variables, loop through this array and replace each one with its corresponding value
centers = ["x1", "y1", "x2", "y2"]
#since these HAVE to be > 0, loop through separately
lengths = ["w1", "h1", "w2", "h2"]

for i in range(0, len(centers)):
    good = False
    while not(good):
        temp = input(centers[i] + ": ")
        #positive or negative int
        if temp.isdigit() or (temp.startswith("-") and temp[1:].isdigit()):
            good = True
            centers[i] = int(temp)
        #invalid or float
        else:
            try:
                temp = float(temp)
                good = True
                centers[i] = float(temp)
            except ValueError:
                print("Incorrect input, try again.")

for i in range(0, len(lengths)):
    good = False
    while not(good):
        temp = input(lengths[i] + ": ")
        #positive int
        if temp.isdigit():
            if int(temp) > 0:
                good = True
                lengths[i] = int(temp)
            else:
                print("Incorrect input, try again.")
        #invalid or float
        else:
            try:
                temp = float(temp)
                if float(temp) > 0:
                    good = True
                    lengths[i] = float(temp)
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect input, try again.")

#transfer all the variables
x1 = centers[0]
y1 = centers[1]
x2 = centers[2]
y2 = centers[3]
w1 = lengths[0]
h1 = lengths[1]
w2 = lengths[2]
h2 = lengths[3]

#top left point, rectangle 1
tl1 = [x1 - (w1/2), y1 + (h1/2)]
#bottom right point, rectangle 1
br1 = [x1 + (w1/2), y1 - (h1/2)]
#top left point, rectangle 2
tl2 = [x2 - (w2/2), y2 + (h2/2)]
#bottom right point, rectangle 2
br2 = [x2 + (w2/2), y2 - (h2/2)]

print(tl1, br1, tl2, br2)

overlap = True

#see if any of the points "intersect"
if not(tl1[0] + w1 >= tl2[0]) and not(tl1[0] <= tl2[0] + w2) and not(tl1[1] + h1 >= tl2[1]) and not(tl1[1] <= tl2[1] + h2):
    overlap = False

if overlap:
    #figure out if its an overlap or if r2 is inside r1
    if (tl1[0] <= tl2[0] and tl1[1] >= tl2[1]) and (br1[0] >= br2[0] and br1[1] <= br2[1]):
        print("r2 is inside of r1.")
    else:
        print("r2 overlaps r1.")
else:
    #no overlap haha
    print("r2 does not overlap r1.")
