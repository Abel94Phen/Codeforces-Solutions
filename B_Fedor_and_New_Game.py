n, m, k = map(int, input().split())

players = []

for _ in range(m + 1):
    players.append(int(input()))


me = players.pop()
possible = 0
for player in players:
    count, i = 0, 0
    bitmask = 1
    player ^= me
    while player:
        if player&1:
            count += 1
        player >>=1
    if count <= k:
        possible += 1

print(possible)
