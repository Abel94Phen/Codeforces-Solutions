t = int(input())
for _ in range(t):
    n = int(input())
    path = input()
    curr = 0
    coins = 0
    while curr < n:
        if path[curr] == '@':
            coins += 1
        
        if curr + 1 < n and path[curr + 1] != '*':
            curr += 1
        elif curr + 2 < n and path[curr + 2] != '*':
            curr += 2
        else:
            break
    print(coins)

