
#2-DIGIT NUMBER
import random as rand

#pick a random 2-digit number
lottery_input = rand.randint(10, 99)
good_input = False
user_input = 0
#put a loop until a valid input is given
while not(good_input):
    temp = input("Enter a 2-digit number: ")
    if temp.isdigit() and len(str(temp)) == 2:
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
    #if modulo produces 9, then the bigger number went into the smaller number once and the difference is 9
    if user_input - lottery_input == 9:
        print("you win $3000")
        win = True
    elif lottery_input - user_input == 9:
        print("you win $3000")
        win = True

#might overlap with the first or second rule, so wrap in an if statement
if not(win):
    lott_arr = []
    user_arr = []
    
    for letter in str(lottery_input):
        lott_arr.append(letter)
    for letter in str(user_input):
        user_arr.append(letter)

    #check each digit in the lottery number to each digit of the user number
    for i in lott_arr:
        for j in user_arr:
            if i == j:
                print("you win $1000")
                win = True
                break

if not(win):
    print("you lose haha")

