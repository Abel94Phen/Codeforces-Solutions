t = int(input())
for _ in range(t):
    n = int(input())
    constraint = input()
    left, right = 1, n
    result = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if constraint[i - 1] == '<':
            result[i] = left
            left += 1
        else:
            result[i] = right
            right -= 1
    print(*result)