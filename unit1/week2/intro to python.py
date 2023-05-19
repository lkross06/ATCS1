#single line comment
'''
double line comment

'''

print("print something on the screen")

'''
5 fundamental types of data
1. int
2. float
3. complex
4. String
5. Boolean

other important data types
6. list
7. tuple
8. set
9. frozen set
10. Dictionary


terminology:

:  colon
;  semicolon
'' single quotes
"" double quotes
/  slash
// double slash
'''


'''
casting can be done using the name of the data type as a function

int()
float()
complex()
str()
bool()
'''
var = 10 #this is an int
str(var) #cast to string
print(var) #returns "10"

'''
input() takes data from the console (user input) and uses it

num = input("enter number : ")
(type a number and press enter, your input becomes the value of num)
'''
num = input("enter number: ")
print("your number was ", num, sep="")


'''
using a comma will concatenate. the sep parameter controls the character
in between each input (by default a space)
'''

print("FFFFFF  U    U   N     N")
print("F       U    U   NN    N")
print("F       U    U   N N   N")
print("FFF     U    U   N  N  N")
print("F       U    U   N   N N")
print("F        UUUU    N    NN")

'''
escape sequences

\n new line
\t tab
\r carriage return
\b backspace

using \" or \' lets you use the quote inside a string (if the string is wrapped with the same character)
'''

#if you wrap string with " " and use ' ' inside (and vice versa), no need for backslash
print("no quotes here but \"quotes here\" yay!")
print('no quotes here but \'quotes here\' yay!')

'''
arithmatic

+   addition
-   subtraction
*   multiplication
**  exponent
\   division (float)
\\  division (int)
%   modulo
'''

print(2 ** 5)
print(10 // 5)
print(10 / 5)

'''
logical operators:

True        true
False       false
a and b     and
a or b      or
not(a)      not


relational operators:

<   less than
>   greater than
<=  less than or equal to
>=  greter than or equal to
==  equal to
!=  not equal to
'''

#notice how this is a string
bool_statement = "1 == 1"
print("The statement", bool_statement, "is", str(bool(bool_statement))) #cast the string to a boolean, get True, cast back to string

'''
modules:

import modules using "import ____"

import modules and save to an object using "import ____ as ___"

import certain functions from module with "import ___ from ___"


conditionals:

if bool statement:
    put action here
elif bool statement:
    put action here
else:
    put action here


loops:

while bool statement:
    put action here

for i in sequence:
    put action here

- if you put a string for the range, it will loop through every character in the string!

range(min, max) function
- lets you loop through a range of integers from min (inclusive) to max (inclusive)


'''
import random
#simple game: addition quiz
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
question = "What is " + str(num1) + " + " + str(num2) + "? "
userAns = input(question)
if userAns == num1 + num2:
    print("Correct!")
else:
    print("NO YOU FOOL! The answer was", num1+num2)

'''
functions

def function_name(a, b):
    put action here
    return x
    
function_name(1, 2)
'''
