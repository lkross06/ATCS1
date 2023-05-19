#external data values
rates = [0, 0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
bounds = [
    [0, 8350, 33950, 82250, 171550, 372950], 
    [0, 16700, 67900, 137050, 208850, 372950], 
    [0, 8350, 33950, 68525, 104425, 186475], 
    [0, 11940, 45500, 117450, 190200, 372950]
    ]

#guide for first input
print("\t0 : single", "\t1 : married filing jointly", "\t2 : married filing separately", "\t3 : head of household", sep="\n")

good_status = False
good_income = False
status = 0
income = 0
#put a loop until a valid input is given
while not(good_status):
    temp_status = input("What is your filing status? ")
    if not(temp_status != "0" and temp_status != "1" and temp_status != "2" and temp_status != "3"):
        good_status = True
        status = int(temp_status)
    else:
        print("Incorrect input, try again.")
#put a loop until a valid input is given
while not(good_income):
    temp_income = input("What is your income? ")
    if temp_income.isdigit():
        good_income = True
        income = int(temp_income)
    else:
        print("Incorrect input, try again.")

tax = 0
top_bound = 0

#get the top bound (which category the income is below)
for i in bounds[status]:
    if i < income:
        top_bound += 1

#now calculate tax per category
temp_income = income
for i in range(0, top_bound + 1):
    temp = temp_income
    if bounds[status][i] < temp:
        temp = bounds[status][i]
    tax += (rates[i] * temp)
    temp_income -= bounds[status][i]

#print out final tax :)
print("Final tax: " + str(tax))

