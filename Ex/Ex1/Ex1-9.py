prices = {'apple' : 1500, 'orange' : 1000, 'pear' : 2000, 'banana' : 500, 'pineapple' : 3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

totalPrice = 0

newDict = {}
newList = []
newSet = {}

for i in my_basket:
    cnt = my_basket.count(i)
    newDict[i] = cnt
print(newDict)

for i in my_basket:
        newList.append(i)
        newSet = set(newList)

print(newSet)

for i in list(newSet):
    totalPrice += prices.get(i) * newDict.get(i)

print(totalPrice)
