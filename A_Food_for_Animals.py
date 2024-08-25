t = int(input())

for _ in range(t):
    a, b, c, x, y = map(int, input().split())

    x = 0 if a >= x else x - a
    y = 0 if b >= y else y - b

    if x + y <= c:
        print("YES")
    else:
        print("NO")