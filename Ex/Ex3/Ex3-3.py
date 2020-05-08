def g_adder(*args):
    sum = args[0]
    for i in args[1:]:
        sum += i
    return sum

#3-1
print(g_adder("hi", "hello"))
print(g_adder(['hufs', 'ice'], [201602560, 'lee']))
print(g_adder(1, 2))

#3-2
print(g_adder(["hi", "hello"], 2))

#3-3
print(g_adder({'a' : 1}, {'b' : 2}))