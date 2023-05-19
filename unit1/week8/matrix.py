#Lucas Ross 12 Oct. 2022

#get the numrows
while True:
    numrows = int(input("Enter the number of rows in the matrix: "))
    if numrows < 5:
        _ = input("Invalid input. Number of rows must be at least 5. Press Enter to continue. ")
    else:
        break

raw = []

print("Enter the matrix row by row:")

#get the matrix itself
for i in range(0, numrows):
    while True:
        row = input()
        if len(row) != numrows:
            _ = input("Invalid input. Each row must be length " + str(numrows) + ". Press Enter to re-enter the current row. ")
        else:
            raw.append(row)
            break

matrix = []

#parse the raw matrix
for i in raw:
    temp = []
    for j in i: #each character in string
        temp.append(int(j))
    matrix.append(temp)

'''
(big oh n^2)
returns an array of the indices and size of the first and largest submatrix without 0, or False is none are found.

matrix      the matrix to get submatrix from
'''
def find_first_squareblock(matrix):
    rtn = False
    found = False
    size = 3
    for r in range(0, len(matrix)):
        for c in range(0, r+1):
            #apply a filter over each spot to look at a 3x3
            sq = getsquare(matrix, len(matrix), r, c, size)
            if not(0 in sq): #if its all 1
                #find the largest size possible
                while not(found):
                    size += 1
                    sq = getsquare(matrix, len(matrix), r, c, size)
                    if 0 in sq:
                        '''
                        subtract 1 from size bc we are testing one size larger each time, and if that fails,
                        we know the largest possible is one lower
                        '''
                        rtn =  [r, c, size - 1]
                        found = True
    return rtn #if no submatrices are found just return false :(

'''
(big oh n^2)
returns an array of all the values of a submatrix in the matrix.
if any values are outside of the matrix, 0 is filled for that value.

example:

1 2 3
4 5 6
7 8 9

would be represented as 

[1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix      matrix to get submatrix from
nr          number of rows/cols in matrix
row         row index to start submatrix at (inclusive)
col         column index to start submatrix at (inclusive)
s           size of submatrix         
'''
def getsquare(matrix, nr, row, col, s):
    rtn = []
    for i in range(row, row + s):
        if i < nr:
            for j in range(col, col + s):
                if j < nr:
                    rtn.append(matrix[i][j])
                else:
                    rtn.append(0) #fill that column with zeros if its outside the matrix
        else:
            for i in range(0, s):
                rtn.append(0)

    return rtn

sub = find_first_squareblock(matrix)

if not(sub):
    print("There are no square submatrices in this matrix.")
else:
    print("The first square submatrix is at (" + str(sub[0]) + ", " + str(sub[1]) + ") with size " + str(sub[2]))
