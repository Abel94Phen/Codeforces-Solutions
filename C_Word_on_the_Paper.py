t = int(input())
for _ in range(t):
    matrix = []
    for _ in range(8):
        matrix.append(input())
    for row in matrix:
        for col in range(8):
            if row[col] != '.':
                break
        if row[col] != '.':
            print(row[col], end = '')
    print()