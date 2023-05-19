'''
pandas library

- data manipulation, analysis, and cleaning
- works with taular data with different data types, lists, etc.
data frame:
- 2-dimensional data structure, used for pandas
'''
import pandas as pd

#first make a hashmap
data = {"data 1":[1, 2, 3, 4, 5, 6],
    "data 2":[1000, 700, 6000, 1000, 400, 350],
    "data 3":[20, 20, 23, 15, 10, 34]}

#make a new data frame from the hashmap
df = pd.DataFrame(data)
print(df)

'''
slicing
- takes a subset of the data frame

head(x)
- takes x rows from the top (default 5 rows)

tail(x)
- takes x rows from the bottom (default 5 rows)
'''
print()
print("HEAD OF DATA FRAME (2 rows):", df.head(2), sep="\n")
print()
print("TAIL OF DATA FRAME (3 rows):", df.head(3), sep="\n")

#or import data frame from csv (csv stores data in a tabular form)
'''
the home directory in vscode is the directory that is currently open (on the explorer tab)
so you may have to either change home directory or use a relative link
'''
income = pd.read_csv("week4/intro_to_machine_learning/income.csv")
print()
print("DATA FRAME FROM income.csv:", income, sep="\n")

#change column data type
income.Y2008 = income.Y2008.astype(float)
print(income.dtypes) #get data types

#get dimensions
print(income.shape)

#gert 

