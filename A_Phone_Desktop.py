t = int(input())

for _ in range(t):
    ones, twos = map(int, input().split())

    screens = 0
    while twos > 1:
        twos -= 2
        if ones > 7:
            ones -= 7
        else:
            ones = 0
        screens += 1

    if twos:
        screens += 1
        if ones >= 11:
            ones -= 11
        else:
            ones = 0

    
    screens += ones // 15 + int(ones%15 != 0)
    print(screens)
