print("Enter/Paste your content.")
import sys

contents = []
while True:
    new = sys.stdin.readline().strip("\n") #reads each line's raw text
    if new == "0":
        break
    else:
        contents.append(new)

print(contents)