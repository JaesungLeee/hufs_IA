def dict_Add(dic1, dic2):
    newDict = dic1
    newDict.update(dic2)
    return newDict

#4-1
print(dict_Add({"a" : 1}, {"b" : 2}))

#4-2
print(dict_Add(['a', 1], ['b', 2]))