def fibonacci(n):
    assert n >= 0 and isinstance(n, int), "n must be a non-negative integer"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for x in range(10):
    print(fibonacci(x))

print(fibonacci(-10))