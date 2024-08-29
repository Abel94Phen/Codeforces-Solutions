t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    total = 0
    for i in range(1, n):
        total += array[i] - array[i - 1]
    print(total)
