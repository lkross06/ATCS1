#3-DIGIT NUMBER
import random as rand

#pick a random 3-digit number
lottery_input = rand.randint(100, 999)
good_input = False
user_input = 0
#put a loop until a valid input is given
while not(good_input):
    temp = input("Enter a 3-digit number: ")
    if temp.isdigit() and len(str(temp)) == 3:
        good_input = True
        user_input = int(temp)
    else:
        print("Incorrect input, try again.")

print("lottery number:", lottery_input)
print("your number:", user_input)

win = False

if user_input == lottery_input:
    print("you win $10000")
    win = True

#might overlap with the first rule, so wrap in an if statement
if not(win):
    lott_arr = []
    user_arr = []
    
    for letter in str(lottery_input):
        lott_arr.append(letter)
    for letter in str(user_input):
        user_arr.append(letter)

    #this is recursion!!! but since there are only 3 cases its not too hard to implement without recursive function
    for i in lott_arr:
        for j in user_arr:
            if i == j:
                #one digit matches (aka third rule)
                lott_arr.remove(i)
                user_arr.remove(j)
                for i2 in lott_arr:
                    for j2 in user_arr:
                        if i2 == j2:
                            #two digits match
                            lott_arr.remove(i2)
                            user_arr.remove(j2)
                            if lott_arr[0] == user_arr[0]:
                                #all three digits match!
                                print("you win $3000")
                                win = True
                                break
                #if the second rule doesnt match, we already know the third rule is satistfied
                #but first we check if the second rule didnt match
                if not(win):
                    print("you win $1000")
                    win = True
                    break

if not(win):
    print("you lose haha")

