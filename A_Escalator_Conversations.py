t = int(input())
for _ in range(t):
    n, m, k, H = map(int, input().split())
    array = list(map(int, input().split()))
    result = 0
    for height in array:
        value = abs(H - height) / k
        if value == int(value) and 0 < value < m:
            result += 1
    print(result)