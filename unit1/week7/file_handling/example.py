#Lucas Ross Oct. 7 2022
print("opening number.txt")

#relative path from workspace (vscode)
with open("week7/file_handling/number.txt", "r+") as f:
    numbers = f.read()

    num = ([eval(x) for x in numbers.split("\n")])
    sum = 0
    for i in num:
        sum += i
    
    #write back result on different lines
    f.write("\n")
    f.write("sum: " + str(sum))

print("file closed automatically")