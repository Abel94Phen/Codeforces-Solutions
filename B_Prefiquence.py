t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a, b = input(), input()
    memo = [0 for _ in range(m)]
    if a[0] == b[0]:
        memo[0] = 1
    for i in range(1, m):
        if memo[i - 1] != n and b[i] == a[memo[i - 1]]:
            memo[i] = memo[i - 1] + 1
        else:
            memo[i] = memo[i - 1]
    print(memo[-1])