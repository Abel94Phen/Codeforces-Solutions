t = int(input())
for _ in range(t):
    grid = [input(), input(), input()]
    if (grid[0][0] == grid[0][1] == grid[0][2] or grid[0][0] == grid[1][0] == grid[2][0]) and grid[0][0] != '.':
        print(grid[0][0])
    
    elif (grid[2][0] == grid[2][1] == grid[2][2] or grid[0][2] == grid[1][2] == grid[2][2]) and grid[2][2] != '.':
        print(grid[2][2])

    elif (grid[0][1] == grid[1][1] == grid[2][1] or grid[1][0] == grid[1][1] == grid[1][2] or grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]) and grid[1][1] != '.':
        print(grid[1][1])
    else:
        print("DRAW")    