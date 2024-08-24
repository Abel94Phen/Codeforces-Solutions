n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


def isthere(target, row, col):
    curr_row, curr_col = [],  []
    for i in range(n):
        if i != col:
            curr_row.append(grid[row][i])
    
    for i in range(n):
        if i != row:
            curr_col.append(grid[i][col])
    
    
    curr_row = set(curr_row)
    curr_col = set(curr_col)
    
    for num in curr_row:
        if target - num in curr_col:
            return True
    
    return False



for i in range(n):
    status = True
    for j in range(n):
        if grid[i][j] != 1:
            target = grid[i][j]
            if not isthere(target, i, j):
                status = False
                break
    if not status:
        print('No')
        break
else:
    print('Yes')