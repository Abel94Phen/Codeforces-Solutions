t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = float('inf')
    for i in range(1, n):
        result = min(result, max(array[i], array[i - 1]) - 1)
    print(result)