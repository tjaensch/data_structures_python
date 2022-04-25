def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        return 2 * powerOfTwo(n - 1)

print(powerOfTwo(5))