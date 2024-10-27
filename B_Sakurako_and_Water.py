from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    diagonals = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                diagonals[i - j].append(matrix[i][j])
    
    result = 0
    for index, diagonal in diagonals.items():
        result += -min(diagonal)
    print(result)