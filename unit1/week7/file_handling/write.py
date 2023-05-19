#Lucas Ross Oct. 7 2022

'''
for .txt or .csv files:

1. opening a file
2. writing/reading a file
3. closing a file
'''

'''
opening a file:

file = open(filename, mode)

filename (string):
- relative path to file
- if you specify a file that doesn't exist, it will create the file!

mode (string):
r+  reading and writing
r   reading only
w+  writing and reading
w   writing only
a+  appending data and reading
a   appending data (to end of file)

- difference between 'a' and 'w': 'a' adds text to end of file, 'w' overwrites text on file
- add 'b' to the end of the mode to make the file reading binary instead of text (if the file is .dat not .txt)
'''

#check if a file exists
from os.path import exists
exist = exists("test.txt")

print("this file does " + ("exist" if exist else "not exist"))

#create a new file/open existing file
file = open("test.txt", "w")
print(file)

#finally close the file
file.close()

'''
File object methods:

read(x)         reads a specific number of characters (x) or all characters from .txt (default) (and returns it)
readline()      reads one line of a .txt file and returns it in a string
readlines()     reads every line of the .txt file and returns it in a list
repr(s)         returns a raw string for s (escape sequence is displayed as literals)
'''


'''
import tkinter.filedialog

askopenfilename()       prompts the user to open a file and returns the file path 
asksavefilename()       promts the user to save a file into a directory
'''

'''
with statement
- automatically closes the file object once all statements have been executed
- not closing file = operating system might not save resources in file

with open() as file_object_name:
    statement1
    statement2
    ...
'''