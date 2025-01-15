t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = a[-1]
    for i in range(n - 1):
        result += max(0, a[i] - b[i + 1])
    print(result)
