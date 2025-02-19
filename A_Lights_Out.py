grid = [list(map(int, input().split())) for _ in range(3)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = [[1 for _ in range(3)] for _ in range(3)]
def inbound(x, y):
    return 0 <= x < 3 and 0 <= y < 3
for i in range(3):
    for j in range(3):
        if grid[i][j]%2:
            result[i][j] = 1 - result[i][j]
            for dx, dy in directions:
                curr_x, curr_y = i + dx, j + dy
                if inbound(curr_x, curr_y):
                    result[curr_x][curr_y] = 1 - result[curr_x][curr_y]
for row in result:
    print("".join(map(str, row)))