t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [i for i in range(1, n + 1)]
    added = 0
    for i in range(n):
        b[i] += added
        if a[i] == b[i]:
            b[i] += 1
            added += 1
    print(b[-1])