import time
'''
takes a variable, prompts the user to enter temp, and changes the variable to that value

temp: user-entered temperature
'''
def get_temp():
    temp = 0
    good_temp = False
    #put a loop until a valid input is given
    while not(good_temp):
        temp_temp = input("Enter the substance's temperature (Celsius): ")
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

curr = get_temp()
while curr > 102.5:
    print("Turn off the thermostat, wait 5 minutes, and try again.")
    time.sleep(5)
    curr = get_temp(curr)

print("yay you're done!")