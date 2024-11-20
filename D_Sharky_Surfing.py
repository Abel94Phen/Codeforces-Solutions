t = int(input())
for _ in range(t):
    n, m, L = map(int, input().split())
    hurdles, gains = [], []
    for _ in range(n):
        hurdles.append(tuple(map(int, input().split())))
    for _ in range(m):
        gains.append(tuple(map(int, input().split())))

    