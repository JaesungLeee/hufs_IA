# Q7.
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
#
# Hints: Use set() and &= to do set intersection operation

list1 = [1, 2, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

set1 = set(list1)
set2 = set(list2)

set1 &= set2
set1 = list(set1)
print(set1)