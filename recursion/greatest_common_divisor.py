def gcd(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    assert a > 0 and b > 0

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(8,12))