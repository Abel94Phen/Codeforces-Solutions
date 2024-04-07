t = int(input())
for _ in range(t):
    target = []
    for row in range(10):
        target.append(input().split())
    points = 0
    for i in range(10):
        for j in range(10):
            if target[i][j] == 'X':
                points += (i + 1)