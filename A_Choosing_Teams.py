n, k = tuple(map(int, input().split()))
array = list(map(int, input().split()))

array.sort()
players = 0

i = 0
while i < n and 5 - array[i] >= k:
    players += 1
    i += 1

print(players // 3)
