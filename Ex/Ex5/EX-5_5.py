# Q5.
# Write a program which can filter even numbers in a list by using range() for loops and list.append().
# The list is:
# [1,2,3,4,5,6,7,8,9,10]
# Hint: Use range() for loops. Use list.append() to add values into a list.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
out_list = []

for i in range(len(list)):
    if i % 2 == 0:
        out_list.append(i)

print(out_list)