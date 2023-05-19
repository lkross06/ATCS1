from math import floor

#translation guide
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

'''
(function from problem 7)
gets the number of days in a month given certain rules of gregorial calendar

month: which month of the year (1-12)
isleap: true if the year is a leap year, false otherwise
'''
def getnumdays(month, isleap):
    numdays = 0
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
    return numdays

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

#check for leap year
if yr % 4 == 0:
    isleap = True

good_day = False
day = 0
#put a loop until a valid input is given
while not(good_day):
    temp_day = input("What day of the month (1-31)? ")
    if temp_day.isdigit():
        temp_day = int(temp_day)
        if temp_day > 0 and temp_day <= getnumdays(month, isleap):
            good_day = True
            day = temp_day
        else:
            print("Incorrect input, try again.")
    else:
        print("Incorrect input, try again.")

'''
using formula from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html


'''

#parse month to fit formula parameters
if month < 3:
    parsed_month = month + 10
else:
    parsed_month = month - 2

#get century and year of century
if len(str(yr)) == 4:
    century = int(str(yr)[0:2])
    yr_end = int(str(yr)[2:])
else:
    century = int(str(yr)[0:1])
    yr_end = int(str(yr)[1:])

if month < 3:
    yr_end -= 1

#make a bunch of temp variables
t1 = floor((2.6 * parsed_month))
t2 = -2 * century
t3 = floor(yr_end/4)
t4 = floor(century/4)

week = (day + t1 + t2 + yr_end + t3 + t4 ) % 7

print(months[month - 1] + " " + str(day) + ", " + str(yr) + " is a " + weekdays[week])