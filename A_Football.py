players = input()
left = 0
for right in range(1, len(players)):
    if players[right] != players[right - 1]:
        if right - left > 6:
            print('YES')
            break
        left = right
else:
    if right - left + 1 > 6:
        print('YES')
    else:
        print('NO')