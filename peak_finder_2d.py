import numpy as np

#Function to defined a random matrix with enough numbers
def generate_random_matrix(m,n):
    #Define lower and upper bounds for the random nos, and then a random vector of size m*n
    ll = 0
    nos = m*n
    ul = 10 *nos
    randomlist = np.random.randint(ll, ul, size=nos)
    matrix = []
    count = 0
    #Feed in the numbers to an empty array
    for i in range(0, m):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(randomlist[count])
            count += 1
    return(matrix)

#Function to calculate max of 2 values
def max2(a,b):
    if a > b:
        return a
    else:
        return b

#Function to calculate max of a list
def maxfinder(array, start, stop, n):
    mid = (start+stop)//2
    if mid > 0 & mid < n-1 & start != stop:
        return(max2(maxfinder(array, start, mid, n), maxfinder(array, mid, stop, n)))
    else:
        return mid

#Function to find 2D peaks
def peakfinder_2d(matrix, startrow, endrow, nrows):
    midrow = (startrow + endrow)//2
    n = len(matrix[midrow])
    midrow_maxind = maxfinder(matrix[midrow], 0, n-1, n)
    if (midrow == startrow) | (midrow == endrow) | (matrix[midrow][midrow_maxind] >= matrix[midrow-1][midrow_maxind] & matrix[midrow][midrow_maxind] >= matrix[midrow+1][midrow_maxind]):
        return [midrow, midrow_maxind]
    elif (midrow > 0) & matrix[midrow][midrow_maxind] <= matrix[midrow+1][midrow_maxind]:
        return peakfinder_2d(matrix, midrow+1, endrow, nrows)
    else:
        return peakfinder_2d(matrix, startrow, midrow, nrows)


#Get user inputs to decide size of the matrix to be constructed
m = int(input("Enter the no. of rows in the matrix"))
n = int(input("Enter the no. of cols in the matrix"))

matrix = generate_random_matrix(m,n)
# row1 = matrix[0]
# n = len(row1)
# max1 = maxfinder(row1, 0, (n-1), n)
# print(row1)
# print(max1)
nrows = len(matrix)
# print(matrix)
print(peakfinder_2d(matrix, 0, nrows - 1, nrows))