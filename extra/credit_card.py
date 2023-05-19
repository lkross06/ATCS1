#Lucas Ross 29 Nov. 2022

import pandas as pd

#get metrics from user
bal = float(input("Credit Card Balance ($): "))
apr = float(input("APR (%): ")) / 100 #convert xx.xx% to 0.xxxx
pay = float(input("Monthly Payment ($): "))

#incrementing values
months = 0
total = 0

def format_dec(n): #concatenates floats to 2 decimal places
    return "${:,.2f}".format(n)

'''
columns:
month   bal     amount_paid     apr     total_paid
'''
#initial record (when the charge is made)
data = [[months, format_dec(bal), format_dec(0), apr, format_dec(total)]]

if pay <= 0: #if balance never decreases :(
    print("You will never pay it off :(")
    quit()

while bal > 0:
    
    #OWEn+1 = (OWEn + NCn - PMTn)(1 + (APR/12)) + FEEn
    bal = (bal - pay) * (1 + (apr/12))

    #increment the things
    total += pay
    months += 1

    if bal < 0: # get the remaining balance left (if the balance isnt divisible by the monthly payment)
        total += bal
        bal = 0

    #new record
    data.append([months, format_dec(bal), format_dec(pay), apr, format_dec(total)])

    if bal == float("inf"): #if the monthly payment is too small
        print("You will never pay it off :(")
        quit()

df = pd.DataFrame(data, columns=["Month", "Balance", "AmountPaid", "APR", "TotalPaid"]) #format data

print(df)



