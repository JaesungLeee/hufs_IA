def star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end='')
        print()

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print("*", end='')
        print()

star_pattern(5)
star_pattern(6)

def star_pattern2(n):
    for i in range(1, n+1):
        print("*"*i)

star_pattern2(5)