t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    operations = 0
    for i in range(n - 1):
        array[i + 1] = max(0, array[i + 1] - operations)
        if array[i] > array[i + 1]:
            operations += array[i]
            array[i + 1] = 0
    print(operations)