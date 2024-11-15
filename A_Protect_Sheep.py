R, C = map(int, input().split())
matrix = []
for _ in range(R):
    matrix.append(list(input()))

def inbound(x, y):
    return 0 <= x < R and 0 <= y < C

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
impossible = False
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'W':
            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if inbound(new_x, new_y):
                    if matrix[new_x][new_y] == 'S':
                        impossible = True
                    elif matrix[new_x][new_y] == '.':
                        matrix[new_x][new_y] = 'D'
if impossible:
    print("No")
else:
    print("Yes")
    for row in matrix:
        print("".join(row))