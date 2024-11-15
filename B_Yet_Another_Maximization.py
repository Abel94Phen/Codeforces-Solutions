t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    result = 0
    for i in range(k):
        maximum, index = 0, i
        while index < n:
            maximum = max(maximum, array[index])
            index += k
        result += maximum
    print(result)