a, b = list(map(int, input().split()))

def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

for i in range(a + 1, b):
    if isPrime(i):
        print("NO")
        exit(0)

if isPrime(b):
    print("YES")
else:
    print("NO")