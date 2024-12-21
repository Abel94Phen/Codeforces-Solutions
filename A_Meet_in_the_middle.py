t = int(input())
for _ in range(t):
    x, y, a, b = map(int, input().split())
    t = (y - x)/(a + b)
    if t != int(t):
        print(-1)
    else:
        print(int(t))