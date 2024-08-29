t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    adds = 0
    for i in range(n - 1):
        x, y = min(array[i], array[i + 1]), max(array[i], array[i + 1])
        while 2*x < y:
            adds += 1
            x *= 2
    print(adds)
