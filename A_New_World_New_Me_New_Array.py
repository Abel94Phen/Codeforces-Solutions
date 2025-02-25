t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    k = abs(k)
    if k//p + int(k%p != 0) <= n:
        print(k//p + int(k%p != 0))
    else:
        print(-1)