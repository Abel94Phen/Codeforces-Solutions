t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    result = 0
    result += (m - 1) * (n - r)
    result += m * (n - r)
    result += m - c
    print(result)