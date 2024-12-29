def leastDivisor(n):
    d = 2
    while d * d <= n:
        if n%d == 0:
            return d
        d += 1
    return n

n = int(input())
score = n
while n > 1:
    divisor = leastDivisor(n)
    score += n // divisor
    n //= divisor
print(score)