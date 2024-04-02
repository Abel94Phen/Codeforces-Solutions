t = int(input())

for _ in range(t):
    corners = []
    for _ in range(4):
        corners.append(list(map(int, input().split())))
    side = max(corners[i][0] for i in range(4)) - min(corners[i][0] for i in range(4))
    print(side ** 2)