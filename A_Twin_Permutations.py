t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]
    for i in range(n):
        b[i] = (n + 1) - a[i]
    print(*b)