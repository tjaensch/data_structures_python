def factorial(n):
    assert n >= 0 and type(n) == int
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-4))