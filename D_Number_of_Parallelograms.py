t = int(input())
points = []
for _ in range(t):
    points.append(tuple(map(int, input().split())))
mids = {}
for i in range(t):
    for j in range(i + 1, t):
        mid = ((points[i][0] + points[j][0])/2, (points[i][1] + points[j][1])/2)
        mid = hash(mid)
        mids[mid] = mids.get(mid, 0) + 1

result = 0
for points in mids:
    result += mids[points] * (mids[points] - 1) // 2
print(result)
