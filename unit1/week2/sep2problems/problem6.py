#translation guide
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#guide for first input
print(
    "\t0 : sunday",
    "\t1 : monday",
    "\t2 : tuesday",
    "\t3 : wednesday",
    "\t4 : thursday",
    "\t5 : friday",
    "\t6 : saturday",
    sep="\n"
)

good_day = False
day = 0
#put a loop until a valid input is given
while not(good_day):
    temp_day = input("What is the day of the week today? ")
    if temp_day.isdigit():
        if int(temp_day) >= 0 and int(temp_day) <= 6:
            good_day = True
            day = int(temp_day)
    else:
        print("Incorrect input, try again.")


good_future_days = False
future_days = 0
#put a loop until a valid input is given
while not(good_future_days):
    temp_future_days = input("How many days in the future? ")
    if temp_future_days.isdigit():
            good_future_days = True
            future_days = int(temp_future_days)
    else:
        print("Incorrect input, try again.")

future_day = (future_days + day) % 7

print("Today is " + days[day] + " and " + str(future_days) + " day(s) from now it will be " + days[future_day] + ".")
