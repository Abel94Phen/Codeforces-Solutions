t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    cost = (m - 1) + (m * (n - 1))
    if cost == k:
        print("YES")
    else:
        print("NO")