def power(x, n):
    assert n >= 0, "n must be non-negative"
    assert isinstance(x, int), "x must be an integer"
    
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 4))