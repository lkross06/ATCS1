def getnum(num):
    temp = 0
    good_temp = False
    #put a loop until a valid input is given
    while not(good_temp):
        temp_temp = input("Enter Number " + str(num) + ": ")
        if temp_temp.isdigit() or (temp_temp.startswith("-") and temp_temp[1:].isdigit()):
            good_temp = True
            temp = int(temp_temp)
        else:
            try:
                temp = float(temp_temp)
                good_temp = True
            except ValueError:
                print("Incorrect input, try again.")
    return temp

#get first two inputs
num1 = getnum(1)
num2 = getnum(2)
#print menu
print("\t1.addition", "\t2.subtraction", "\t3.multiplication", "\t4.division", "\t5.modulus",sep="\n")
op = 0
good = False
#put a loop until a valid input is given
while not(good):
    temp = input("Enter Operation: ")
    if temp.isdigit():
        if int(temp) > 0 and int(temp) < 6:
            good = True
            op = int(temp)
        else:
            print("Incorrect input, try again.")
    else:
        print("Incorrect input, try again.")

operations = ["+", "-", "*", "/", "%"]
final = 0
if op == 1:
    final = num1 + num2
if op == 2:
    final = num1 - num2
if op == 3:
    final = num1 * num2
if op == 4:
    final = num1 / num2
if op == 5:
    final = num1 % num2

print(str(num1) + " " + operations[op - 1] + " " + str(num2) + " = " + str(final))