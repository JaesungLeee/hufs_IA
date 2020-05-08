# Q6.
# Write a program which can filter even numbers in a list by using list comprehension. The list is:
#
# [1,2,3,4,5,6,7,8,9,10]
# Hint: Use list comprehension

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
out_list = [i for i in num_list if i % 2 == 0]
print(out_list)