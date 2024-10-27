def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(input())
for _ in range(t):
    k = int(input())
    print(100 // gcd(k, 100))