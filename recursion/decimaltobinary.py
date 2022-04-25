def decimaltobinary(n):
    assert n >= 0 and isinstance(n, int), "n must be a non-negative integer"

    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimaltobinary(n//2)

print(decimaltobinary(13))