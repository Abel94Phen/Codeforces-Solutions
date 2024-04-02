t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    while n > 0:
        grid.append(input())
        n -= 1
    
    row = 0
    while grid[row].count('1') == 0:
        row += 1
    
    if grid[row].count('1') != grid[row + 1].count('1'):
        print("TRIANGLE")
    else:
        print('SQUARE')