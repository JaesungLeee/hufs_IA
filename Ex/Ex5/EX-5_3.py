# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,∼Y-1.
# Suppose the following inputs are given to the program:
# 3,5

# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

row_column = input("Enter the row number : ").split(',')
row = int(row_column[0])
column = int(row_column[1])

zero_setting_list = [[0 for j in range(column)] for i in range(row)]
# print(zero_setting_list)

array = zero_setting_list
for i in range(row):
    for j in range(column):
        array[i][j] = i*j

print(array)