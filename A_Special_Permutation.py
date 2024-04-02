t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    for i in range(1, n + 1):
        result.append(i)

    for i in range(n - 1):
        result[i], result[i + 1] = result[i + 1], result[i]

    print(*result)