t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total += abs(i - n)
        n -= 1
    print(total // 2 + 1)