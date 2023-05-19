#translation guide
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

good_month = False
month = 0
#put a loop until a valid input is given
while not(good_month):
    temp_month = input("What month of the year (1-12)? ")
    if temp_month.isdigit():
        temp_month = int(temp_month)
        if temp_month > 0 and temp_month <= 12:
            good_month = True
            month = temp_month
        else:
            print("Incorrect input, try again.")
    else:
        print("Incorrect input, try again.")

good_yr = False
yr = 0
#put a loop until a valid input is given
while not(good_yr):
    temp_yr = input("What year? ")
    if temp_yr.isdigit():
        temp_yr = int(temp_yr)
        good_yr = True
        yr = temp_yr
    else:
        print("Incorrect input, try again.")

isleap = False
numdays = 0

#check for leap year
if yr % 4 == 0:
    isleap = True

if month <= 7:
    if month % 2 == 1:
        numdays = 31
    elif month == 2:
        #handle february separately
        if isleap:
            numdays = 29
        else:
            numdays = 28
    else:
        numdays = 30
else:
    if month % 2 == 0:
        numdays = 31
    else:
        numdays = 30

print("The number of days in " + months[month - 1] + " " + str(yr) + " is " + str(numdays))