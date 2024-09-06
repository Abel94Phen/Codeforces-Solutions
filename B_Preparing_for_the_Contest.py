t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    result = []
    while n - 1 != k:
        result.append(n)
        n -= 1
    for i in range(1, n + 1):
        result.append(i)
    print(*result)