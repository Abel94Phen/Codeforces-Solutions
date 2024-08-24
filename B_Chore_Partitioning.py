n, a, b = map(int, input().split())
chores = list(map(int, input().split()))

chores.sort()

print(chores[b] - chores[b - 1])