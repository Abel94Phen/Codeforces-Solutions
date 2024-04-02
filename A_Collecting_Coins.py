t = int(input())
while t > 0:
    coins = list(map(int, input().split()))
    ave_coins = sum(coins) // 3
    if max(coins[:3]) > ave_coins or sum(coins)%3:
        print("NO")
    else:
        print("YES")
    t -= 1