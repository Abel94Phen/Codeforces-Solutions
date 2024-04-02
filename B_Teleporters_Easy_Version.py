t = int(input())
for _ in range(t):
    n, c = list(map(int, input().split()))
    array = list(map(int, input().split()))
    for i in range(n):
        array[i] += (i + 1)
    array.sort()
    teleporters = 0
    for i in range(n):
        if c < array[i]:
            break
        c -= array[i]
        teleporters += 1
    print(teleporters)