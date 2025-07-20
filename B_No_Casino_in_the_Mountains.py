t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    weather = list(map(int, input().split()))
    left, right = 0, 0
    result = 0
    while right < n:
        if weather[right] == 0:
            right += 1
            if right - left == k:
                result += 1
                right += 1
                left = right
        else:
            right += 1
            left = right
    print(result)