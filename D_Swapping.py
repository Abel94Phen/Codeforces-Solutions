t = int(input())
for _ in range(t):
    n, x, m = map(int, input().split())
    a, b = x, x
    for _ in range(m):
        l, r = map(int, input().split())
        if min(b, r) - max(a, l) >= 0:
            a, b = min(l, a), max(r, b)
    print(b - a + 1)