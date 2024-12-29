n = int(input())
grid = [list(input()) for _ in range(n)]
def isCross(i, j):
    return grid[i][j] == grid[i - 1][j] == grid[i + 1][j] == grid[i][j - 1] == grid[i][j + 1] == '#'

def unDraw(i, j):
    grid[i][j] = grid[i - 1][j] = grid[i + 1][j] = grid[i][j - 1] = grid[i][j + 1] = '.'

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if isCross(i, j):
            unDraw(i, j)

status = True
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            status = False
if status:
    print("YES")
else:
    print("NO")
