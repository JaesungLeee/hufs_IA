prices = {'apple' : 1500, 'orange' : 1000, 'pear' : 2000, 'banana' : 500, 'pineapple' : 3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

newDict = {}
for i in my_basket:
    cnt = my_basket.count(i)
    newDict[i] = cnt

print(newDict)
