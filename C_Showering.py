t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())
    max_gap = float("-inf")
    last = 0
    for _ in range(n):
        curr = tuple(map(int, input().split()))
        max_gap = max(max_gap, curr[0] - last)
        last = curr[1]

    max_gap = max(max_gap, m - last)
    if max_gap >= s:
        print("YES")
    else:
        print("NO")