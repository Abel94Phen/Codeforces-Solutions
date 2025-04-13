t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    forward, backward = array[:], array[:]
    for i in range(1, n):
        forward[i] = max(forward[i], forward[i - 1])
    for i in range(n - 2, -1, -1):
        backward[i] = min(backward[i], backward[i + 1])

    for i in range(n - 1):
        if forward[i] > backward[i + 1]:
            print("YES")
            break
    else:
        print("NO")