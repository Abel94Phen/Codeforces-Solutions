t = int(input())
for _ in range(t):
    n = int(input())
    total = (2 ** (n + 1)) - 2
    larger = 2**n
    total -= 2**n
    for i in range(1, (n - 1)//2 + 1):
        larger += 2**i
        total -= 2**i
    print(larger - total)