directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def getAnswer(grid, x, y):

    def inbound(i, j):
        return 0 <= i < x and 0 <= j < y
    
    def dfs(i, j):
        result = grid[i][j]
        grid[i][j] = 0
        stack = [(i, j)]
        while stack:
            curr_x, curr_y = stack.pop()
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if inbound(new_x, new_y) and grid[new_x][new_y]:
                    result += grid[new_x][new_y]
                    grid[new_x][new_y] = 0
                    stack.append((new_x, new_y))
        return result
    
    maxVolume = 0
    for i in range(x):
        for j in range(y):
            if grid[i][j]:
                maxVolume = max(maxVolume, dfs(i, j))
    return maxVolume

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]
    print(getAnswer(matrix, n, m))