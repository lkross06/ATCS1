'''
deleting objects
- delete the object from the program

del obj
'''
num = 5
del num
#now if we try to call it, we cant
try:
    print(num)
except:
    print("num not found :(")

'''
sequences: object storing a collection of data

list: mutable sequence
tuple: immutable sequence (cant change data once initialized)
'''

list1 = ["a", "b", "c", "d", "e"]

'''
indexing lists:

positive index: identify position relative to beginning of list
- index 0 is first element, index 1 is second element

negative index: identify position relative to end of list
- index -1 is last element, index -2 is second-to-last, etc.


'''

print("the last element is " + list1[-1]) #e
print("this first element is " + list1[0]) #a
print("the length of the list is " + str(len(list1))) #5

'''
range(start, stop, step) returns a list

parameters (integer only):
start   number to start at (inclusive)
stop    number to end at (exclusive)
step    how much to increment in-between values
'''
print(list(range(3))) #[0, 1, 2]
print(list(range(5, 50, 10))) #[5, 15, 25, 35, 45]

'''
list slicing
- slice: span of items taken from a sequence

slicing format: list[start:end:step]
- start inclusive, end exclusive
- all params are ints
- default start value: 0
- default end value: len(list)
- default step value: 1
'''

print(list(list1[1:3])) #["b", "c"]

'''
in operator
- returns True if an item is in a list, False otherwise

general format: item in list
'''

print("a" in list1) #True
print("f" in list1) #False

'''
extra functions:

list.append(item)
- adds item to end of a list

list.index(item)
- returns index of a value in a list
- raises ("throws" keyword in Java) ValueError exception if not found

list.remove(item)
- removes and returns item
- raises ValueError exception if not found
'''

'''
list comprehension
- concise way to create items from sequences

format:
a for b in c if d
- a: some sort of statement (usually arithmatic) to differentiate each value (use variable x)
- b: x
- c: sequence to apply operation "a" to
- d: condition to add a value (optional)
'''

list2 = [x for x in range(0, 5)] #[0, 1, 2, 3, 4]
print(list2)
list3 = [0.5 * x for x in list2] #[0.0, 0.5, 1.0, 1.5, 2.0]
print(list3)
list4 = [x for x in list3 if x < 1.5] #[0.0, 0.5, 1.0]
print(list4)

'''
splitting a string to a list: split() function

str.split(x)
- returns a list with the string divided by every instance of string x in string str
'''

str1 = "test1xxtest2xxtest3xxtest4"
list5 = str1.split("xx")
print(list5) #["test1", "test2", "test3", "test4"]

'''
shifting lists (no bitwise operator in python)
- move every value to an index one less than its prev (left) or one more than its prev (right)
- for a left shift, index 0 is moved to index -1 (wrap around the array)
- for a right shift, index -1 is moved to index 0 (wrap around the array)

'''
def shift_left(list):
    temp = []
    for i in list:
        temp.append(i)
    for i in range(0, len(list), 1):
        list[i - 1] = temp[i]
    return list

def shift_right(list):
    temp = []
    for i in list:
        temp.append(i)
    for i in range(-1, len(list) - 1, 1):
        list[i + 1] = temp[i]
    return list

list6 = [1, 2, 3, 4, 5]
print(shift_left(list6)) #[2, 3, 4, 5, 1]
print(shift_right(list6)) #[5, 1, 2, 3, 4]