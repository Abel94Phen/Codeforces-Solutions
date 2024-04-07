t = int(input())
for _ in range(t):
    target = []
    for row in range(10):
        target.append(list(input()))
    points = 0
    for i in range(10):
        for j in range(10):
            if target[i][j] == 'X':
                if 4 <= i <= 5 and 4 <= j <= 5:
                    points += 5
                elif 3 <= i <= 6 and 3 <= j <= 6:
                    points += 4
                elif 2 <= i <= 7 and 2 <= j <= 7:
                    points += 3
                elif 1 <= i <= 8 and 1 <= j <= 8:
                    points += 2
                else:
                    points += 1
    print(points)