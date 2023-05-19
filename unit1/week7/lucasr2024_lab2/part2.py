#Lucas Ross Oct. 5 2022
import random as r

chars = [] #char array
counts = [0 for x in range(0, 26)] #int array

#generate 100 random lowercase letters
for i in range(0, 100):
    chars.append(chr(r.randint(97, 122))) #gets a lowercase ascii value, convert to character

#print the things
print("---- Lowercase Letters ----")
for i in range(0, len(chars)):
    print(str(chars[i]), end=" ")

#count each occurance
for i in chars:
    #get the ascii val
    dec = ord(i) - 97 #97 is lowest value, this will put it on a 0-25 range instead of 97-122 range
    counts[dec] += 1

print("\n\n---- Frequency Table ----")
for i in range(0, len(counts)):
    letter = str(chr(i + 97)) #97 is lowest value, this will put it on a 97-122 range instead of 0-25 range
    print(letter + "\t\t" + str(counts[i]) + "\n")
