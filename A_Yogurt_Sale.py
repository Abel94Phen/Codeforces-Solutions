t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if n%2:
        print(min(a*n, (int((n - 1)*b/2)) + a))
    else:
        print(min(a*n, int(n*b/2)))