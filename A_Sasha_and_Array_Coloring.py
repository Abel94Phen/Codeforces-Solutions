t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    array.sort()
    i, j = 0, length - 1
    cost = 0
    while i < j:
        cost += array[j] - array[i]
        i += 1
        j -= 1
    print(cost)