#Lucas Ross 5 Oct. 2022

import random as r

coins = [0 for i in range(0, 12)]

#pick lighter or heavier
weight = -1 if r.randint(0, 1) == 0 else 1
coins[r.randint(0, len(coins) - 1)] = weight #replace a real with a fake

'''
weighs two sets of items against each other

left    first set of weights
right   second set of weights
returns -1 if left is heavier, 1 if right is heavier, 0 if equal
'''
def scale(left, right):
    wleft = 0
    wright = 0
    for i in left:
        wleft += i
    for i in right:
        wright += i
    
    if wleft > wright:
        return -1
    elif wleft < wright:
        return 1
    else:
        return 0

fake = 0

print(coins)

#step 1: split into 4 groups
a = coins[0:4]
b = coins[4:8]
c = coins[8:12]
#step 2: weigh a / b
step2 = scale(a, b)
if step2 == 0:
    #step 3: weigh 2 c with 2 b (b must not be fake)
    b1 = b[0:2]
    c1 = c[0:2]
    c2 = c[2]
    c3 = c[3]
    step3 = scale(c1, b1)
    if step3 == 0:
        #step 4: weigh one of c with one of b
        step4 = scale([c2], [b1[0]])
        if step4 == 0:
            #if theyre equal, fake is the only one that hasnt been weighed yet
            fake = c3
        else:
            #if its imbalanced, its the c
            fake = c2
    else:
        #step 4: weigh one of the 2 c with one of b
        step4 = scale([c1[0]], [b1[0]])
        if step4 == 0:
            #if theyre equal, fake is the only one that hasnt been weighed yet
            fake = c1[1]
        else:
            #if its imbalanced, its the c
            fake = c1[0]
else:
    #step 3: weigh 3 coins, two of B and one of A and vice versa
    #keep track which one was heavier
    l = [a[0], b[0], b[1]]
    r = [a[1], a[2], b[2]]
    a1 = a[3]
    b1 = b[3]
    step3 = scale(l, r)
    if step3 == 0:
        #step 4: weigh one of a with one of b
        step4 = scale([a1], [r[0]])
        if step4 == 0:
            #if theyre equal, fake is the only one that hasnt been weighed yet
            fake = b1
        else:
            #if its imbalanced, its the a
            fake = a1
    else:
        if step2 == -1:
            #either an a is heavier or a b is lighter
            if step3 == -1:
                #the a in left is heavier or b in right is lighter
                #step 4: weigh a in left against one of c (we know its real)
                step4 = scale([l[0]], [c[0]])
                if step4 == 0:
                    fake = r[2] #b in right
                else:
                    fake = l[0] #a in left
            else:
                exit()
            


print(fake)


