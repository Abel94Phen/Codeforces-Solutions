t = int(input())
for _ in range(t):
    b, c, h = map(int, input().split())
    if b <= c + h:
        print(2 * b - 1)
    else:
        print(2 * (c + h) + 1)