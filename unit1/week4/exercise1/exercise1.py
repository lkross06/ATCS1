#Lucas Ross, Sep. 13 2022

#import modules
import pandas as pd
from matplotlib import pyplot as plt

#get data
#data is automatically formatted with column names and row markers (so when we access data, its only the numbers)
df = pd.read_csv("company_sales_data.csv")

'''
selecting columns of data in data frame
(for some reason, df["column"] was not working on this data frame)

loc[]   String-based indexing
iloc[]  int-based indexing

syntax:
df.loc[a:b, [c, d, e]]

a           row # to start at (inclusive)
b           row # to end at (inclusive)
[c, d, e]   indices of which columns to retrieve
'''
#extracts the first and second columns' data
# print(df.iloc[:,[0, 1]])


#exercise 1

x1 = df.iloc[:, [0]] #month_number column, which is same as row numbers
y1 = df.iloc[:, [8]] #total_profit is column 9, but since its index-based, its 9 - 1 = 8

plt.plot(x1, y1)

plt.title("Company profit per month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")

plt.show()


#exercise 2

#use same data from exercise 1
x2 = x1
y2 = y1
#https://matplotlib.org/stable/api/markers_api.html marker stuff
plt.plot(x2, y2, linewidth=3, linestyle="--", color="red", mfc="k", marker="o", label="Profit Data from Last Year")

plt.title("Company Sales Data from Last Year")
plt.xlabel("Month Number")
plt.ylabel("Sold Units Number")
plt.legend(loc=4) #shows the legend in the bottom-right

plt.show()


#exercise 3

#same x values as exercise 1
x3 = x1
#y values are for each thing
y3_1 = df.iloc[:, [1]]
y3_2 = df.iloc[:, [2]]
y3_3 = df.iloc[:, [3]]
y3_4 = df.iloc[:, [4]]
y3_5 = df.iloc[:, [5]]
y3_6 = df.iloc[:, [6]]

plt.plot(x3, y3_1, label="Face Cream Sales Data", marker=".")
plt.plot(x3, y3_2, label="Face Wash Sales Data", marker=".")
plt.plot(x3, y3_3, label="Toothpaste Sales Data", marker=".")
plt.plot(x3, y3_4, label="Bathing Soap Sales Data", marker=".")
plt.plot(x3, y3_5, label="Shampoo Sales Data", marker=".")
plt.plot(x3, y3_6, label="Moisturizer Sales Data", marker=".")

plt.legend()
plt.title("Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")

plt.show()


#exercise 4

x4 = x1
y4 = y3_3

plt.scatter(x4, y4, label="Toothpaste Sales Data")

plt.grid(True, linestyle="--") #make a grid with dashed lines
plt.title("Toothpaste Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Number of Units Sold")
plt.legend()

plt.show()


#exercise 5

x5_1 = [] #x1
x5_2 = [] #x1 + width (gives offset to the other bars)
y5_1 = [] #y3_1
y5_2 = [] #y3_2

width5 = 0.3 #width of bars

#parse data
for i in range(0, len(x1)):
    x5_1.append(x1.iat[i, 0])
    x5_2.append(x1.iat[i, 0] + width5)
    y5_1.append(y3_1.iat[i, 0])
    y5_2.append(y3_2.iat[i, 0])
    

plt.bar(x5_1, y5_1, label="Face Cream Sales Data", width=width5)
plt.bar(x5_2, y5_2, label="Face Wash Sales Data", width=width5)

plt.legend(loc=2)
plt.grid(True, linestyle="--")
plt.title("Face Wash and Face Cream Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")

plt.show()


#exercise 6

x6 = [] #x1
y6 = [] #y3_4

#parse data
for i in range(0, len(x1)):
    x6.append(x1.iat[i, 0])
    y6.append(y3_4.iat[i, 0])

plt.bar(x6, y6)

plt.title("Bathing Soap Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units per Number")
plt.grid(True, linestyle="--")

plt.show()


#exercise 7

y7 = y1

plt.hist(y7, bins=9, label="Profit Data")

plt.title("Profit Data")
plt.legend(loc=2)
plt.xlabel("Profit Range in Dollars")
plt.ylabel("Actual Profit in Dollars")

plt.show()


#exercise 8

totals8 = []
labels8 = []

#each column with sales data
for i in range(1, 7):
    sum = 0
    #for the index of each row
    for j in range(0, len(df.iloc[:, [i]])):
        #get the value and add it
        sum += df.iloc[:, [i]].iat[j, 0]
    #add sum to totals
    totals8.append(sum)

#now get labels
i = 0
for col in df.columns:
    if i > 0 and i < 7:
        labels8.append(col)
    i+= 1

#format percentage as xx.x%
plt.pie(totals8, labels=labels8, autopct="%1.1f%%")

plt.legend(loc=4)
plt.title("Sales Data")

plt.show()


#exercise 9

x9 = x1
y9_1 = y3_4
y9_2 = y3_2

#this figure has 2 rows, 1 column, this is 1st plot
plt.subplot(2, 1, 1)
plt.plot(x9, y9_1, color="black", marker=".", linewidth=3)

plt.title("Sales Data of Bathing Soap")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")

#2nd plot
plt.subplot(2, 1, 2)
plt.plot(x9, y9_2, color="red", marker=".", linewidth=3)

plt.title("Sales Data of Face Wash")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")

#show the fig
plt.show()


#exercise 10

x10 = [] #x1
y10_1 = [] #y3_1
y10_2 = [] #y3_2
y10_3 = [] #y3_3
y10_4 = [] #y3_4
y10_5 = [] #y3_5
y10_6 = [] #y3_6

labels9 = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]
colors9 = ["blue", "red", "green", "purple", "orange", "brown"]

#convert to arrays to be processed better
for i in range(0, len(x1)):
    x10.append(x1.iat[i, 0])
    y10_1.append(y3_1.iat[i, 0])
    y10_2.append(y3_2.iat[i, 0])
    y10_3.append(y3_3.iat[i, 0])
    y10_4.append(y3_4.iat[i, 0])
    y10_5.append(y3_5.iat[i, 0])
    y10_6.append(y3_6.iat[i, 0])

#plot empty lines for the legend in the corner (make sure colors align!)
for i in range(0, 6):
    plt.plot([], [], color=colors9[i], label=labels9[i])

plt.stackplot(x10, y10_1, y10_2, y10_3, y10_4, y10_5, y10_6, colors=colors9)

plt.legend(loc=2)
plt.title("All Products Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units in Number")

plt.show()