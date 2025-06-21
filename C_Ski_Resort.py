n = int(input())
for _ in range(n):
    n, k, q = map(int, input().split())
    array = list(map(int, input().split()))
    left, right = 0, 0
    result = 0
    while right <= n:
        if right == n or array[right] > q:
            limit = right - left - k + 1
            result += (1 + limit) * limit // 2 if limit > 0 else 0
            left = right + 1
        right += 1
    print(result)