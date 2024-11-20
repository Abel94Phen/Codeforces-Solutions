t = int(input())
for _ in range(t):
    n = int(input())
    if n < 5:
        print(-1)
    else:
        odds = [i for i in range(1, n + 1, 2)]
        evens = [i for i in range(2, n + 1, 2)]

        if n%2 == 0:
            odds[1], odds[-1] = odds[-1], odds[1]
            evens[0], evens[2] = evens[2], evens[0]
            
        else:
            odds[-1], odds[2] = odds[2], odds[-1]
            evens[1], evens[0] = evens[0], evens[1]

        print(*odds, *evens)