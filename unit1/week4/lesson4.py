#part 1

def do_twice(f, val):
    f(val)
    f(val)

def print_spam():
    print('spam')

def print_twice(arg):
    print(str(arg))
    print(str(arg))

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


do_twice(print_twice, "spam")

#part 2

'''
there two possible horizontal lines to be printed: one with a horizontal line (grid1) or one with spaces (grid2)

index 0 : connectors
index 1 : in between
'''
grid1 = ["+", " - - - - "]
grid2 = ["|", "         "]

'''
prints a single line from the array of a given size

n: size of line (in terms of how many spaces)
arr: which arr to print out
'''
def print_line(n, arr):
    for i in range(0, n):
        print(arr[0], arr[1], sep="", end="")
    print(arr[0])

'''
prints a grid of a given size

n: size of grid (in terms of how many spaces by how many spaces)
'''
def draw_grid(n):
    #print top row line
    print_line(n, grid1)

    #print each row
    for i in range(0, n):
        #print each col line
        for j in range(0, 3):
            print_line(n, grid2)
        #print row line
        print_line(n, grid1)

draw_grid(2)

#part 3

# Return true if the card number is valid
def isValid(number):
    sum = getDigit(number)
    if sum % 10 == 0:
        return True
    return False

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    even = [] # store in array because we need to parse each one individually for 2-digit nums
    s = str(number)
    sum = 0
    #add all even places * 2
    for i in range(0, len(s), 2):
        even.append(int(s[i]) * 2)
    #look for 2-digit numbers, otherwise just sum up
    for i in even:
        '''
        all we have to do is check for 2-digit numbers because the largest possible
        value is 9 * 2 which is 18
        '''
        if len(str(i)) == 2:
            #split into 2 strings and cast back to int
            sum += (int(str(i)[0]) + int(str(i)[1]))
        else:
            sum += i
    return sum

# Return this number if it is a single digit, otherwise, return

# the sum of the two digits
def getDigit(number):
    odd = sumOfOddPlace(number)
    even = sumOfDoubleEvenPlace(number)
    return odd + even

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    #first get the odd digits
    s = str(number)
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    return sum


ccn = 0
good_ccn = False
#put a loop until a valid input is given
while not(good_ccn):
    '''
    credit card rules:
    
    - 13-16 digit number
    - starts with:
        - 4 for visa
        - 5 for mastercard
        - 37 for american express
        - 6 for discover
    '''
    temp = input("Enter 13-16 digit credit card number: ")
    if temp.isdigit() and len(temp) >= 13 and len(temp) <= 16:
        if temp.startswith("4") or temp.startswith("5") or temp[:2] == "37" or temp.startswith("6"):
            good_ccn = True
            ccn = int(temp)
        else:
            print("Incorrect input, try again.")
    else:
        print("Incorrect input, try again.")

#print out if the number is valid or not
print(isValid(ccn))