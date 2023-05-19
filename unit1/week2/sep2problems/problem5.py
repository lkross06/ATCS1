#guide for first inputs
print("\tax + by = e", "\tcx + dy = f", sep="\n")

#get values for all 6 variables
variables = ["a", "b", "c", "d", "e", "f"]
for i in range(0, len(variables)):
    good_input = False
    while not(good_input):
        temp_var = input("What is the value of " + variables[i] + "? ")
        #first case: positive integer
        if temp_var.isdigit():
            good_input = True
            variables[i] = int(temp_var)
        #second case: negative integer
        elif temp_var.startswith("-") and temp_var.split("-")[1].isdigit():
            good_input = True
            variables[i] = int(temp_var)
        #third case: either float or invalid
        else:
            #see if the number can be casted to a float (catch ValueError - casting error)
            try:
                float(temp_var)
                good_input = True
                variables[i] = float(temp_var)
            except ValueError:
                print("Incorrect input, try again.")

#now all of the values are stored in order in the variables array

'''
Gaussian Elimination

1. subtraction

        ax + by = e
- (a/c)(cx + dy = f)
---------------------
(b - ((ab)/c))y = e - ((af)/c)

y = (e - ((af)/c))/(b - ((ab)/c))

2. substitution

x = (e - by)/a
'''
a = variables[0]
b = variables[1]
c = variables[2]
d = variables[3]
e = variables[4]
f = variables[5]

y = (e - (((a*f))/c))/(b - (((a*b))/c))

x = (e - (b*y))/a

print("x = " + str(x), "y = " + str(y), sep="\n")