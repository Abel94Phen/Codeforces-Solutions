t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    flips = 0
    for i in range(n):
        if grid[i][-1] == 'R':
            flips += 1
    for i in range(m):
        if grid[n - 1][i] == 'D':
            flips += 1
    print(flips)