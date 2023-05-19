#Lucas Ross Oct. 4 2022
import sys

found = [False for x in range(0, 99)]
user = []

raw = []
print("Input your lotto ticket below. Enter an empty line with a zero (0) to stop input.")

#read lines from terminal until the user is done
while True:
    new = sys.stdin.readline().strip("\n") #reads each line's raw text
    if new == "0":
        break
    else:
        raw.append(new)

#parse raw string for each individual int
for i in raw:
    for j in i.split(" "):
        user.append(int(j))

#mark off each number in the storage lists
for n in user:
    index = int(n)
    found[index - 1] = True

#print result
if False in found:
    print("\nThe ticket does not cover all numbers.")
else:
    print("\nThe ticket does cover all numbers.")