t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = 0
    for i in range(1, n):
        result = max(result, array[i] * array[i - 1])
    print(result)