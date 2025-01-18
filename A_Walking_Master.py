t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    k = d - b
    m = a + k - c
    if m < 0 or k < 0:
        print(-1)
    else:
        print(k + m)