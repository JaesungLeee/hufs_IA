prices = {'apple' : 1500, 'orange' : 1000, 'pear' : 2000, 'banana' : 500, 'pineapple' : 3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

newList = []
newSet = {}
for i in my_basket:
    if i.endswith('e'):
        newList.append(i)
        newSet = set(newList)
print(newSet)