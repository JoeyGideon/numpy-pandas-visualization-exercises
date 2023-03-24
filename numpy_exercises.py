import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
(a<0).sum()
# How many positive numbers are there?
(a>0).sum()
# How many even positive numbers are there?
b = (a>0) & (a%2==0)
np.count_nonzero(b)
# If you were to add 3 to each data point, how many positive numbers would there be?
c = (a+3)
(c>0).sum()
# If you squared each number, what would the new mean and standard deviation be?
d = (a**2)
mean = d.mean()
print(mean)
np.std(d)
d.std()
# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set.
e = a-mean
print(e)
# Calculate the z-score for each data point. Recall that the z-score is given by:
import pandas as pd
import scipy.stats as stats
stats.zscore(a)

# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
# Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
print(mean_of_a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)
print(product_of_a)
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
print(squares_of_a)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
a = np.array(a)
odds_in_a = a[a%2 == 1]
print(odds_in_a)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
a =np.array(a)
evens_in_a = a[a%2 ==0]
print(evens_in_a)
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = ([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = sum(b)
print(sum_of_b)
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = b.min()
print(min_of_b)
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = np.max(b)
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = np.mean(b)
print(mean_of_b)
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b = np.product(b)
print(product_of_b)
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b = np.square(b)
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b = np.array(b)
odds_in_b = b[b%2==1]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
    
b = np.array(b)
evens_in_b = b[b%2==0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.
b = np.array(b)
print(b.shape)

# Exercise 10 - transpose the array b.
np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b, (1,6))
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b, (6,1))
## Setup 3
c = ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_c = np.min(c)
max_c = np.max(c)
sum_c = np.sum(c)
prod_c = np.product(c)
print(min_c)
print(max_c)
print(sum_c)
print(prod_c)
# Exercise 2 - Determine the standard deviation of c.
std_c = np.std(c)
print(std_c)
# Exercise 3 - Determine the variance of c.
var_c = np.var(c)
print(var_c)
# Exercise 4 - Print out the shape of the array c
c = np.array(c)
print(c.shape)
# Exercise 5 - Transpose c and print out transposed result.
np.transpose(c)
# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
# Exercise 7 - Write the code necessary to sum up the result of c times (c transposed). Answer should be 261
k = np.transpose(c)
print(k)
times = c * k
np.sum(times)
# or
np.sum(c*np.transpose(c))
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.product(c*np.transpose(c))

## Setup 4
d = ([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
# Exercise 8 - Print out the shape of d.
np.shape(d)
# Exercise 9 - Transpose and then print out the shape of d.
t = np.transpose(d)
print(np.shape(t))
# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d,(9,2))