def fact1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact1(n-1)

def fact2(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact

print(fact1(5))
print(fact2(5))