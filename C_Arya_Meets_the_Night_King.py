s, b = map(int, input().split())
spaceships = list(map(int, input().split()))
bases = []
for _ in range(b):
    bases.append(list(map(int, input().split())))
bases.sort()
for i in range(1, b):
    bases[i][1] += bases[i - 1][1]
result = [0 for _ in range(s)]
for i in range(s):
    left, right = 0, b - 1
    while left <= right:
        mid = (left + right) // 2
        if bases[mid][0] <= spaceships[i]:
            left = mid + 1
        else:
            right = mid - 1

    if right > -1 and bases[right][0] <= spaceships[i]:
        result[i] = bases[right][1]
print(*result)