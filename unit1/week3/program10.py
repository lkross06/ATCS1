kph = range(60, 131, 10)
mph = []
#get the corresponding mph vals
for i in kph:
    mph.append(i * 0.6214)

#print it all out with two tabs in between
print("KPH", "MPH", sep="\t\t")
print("------------------------")
for i in range(0, len(kph)):
    #format(x, ".2f") truncates the float to 2 decimal places
    print(kph[i], format(mph[i], ".2f"), sep="\t\t")