def sumofdigits(n):
    assert n >= 0, "n must be non-negative"
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits(n // 10)

print(sumofdigits(54))