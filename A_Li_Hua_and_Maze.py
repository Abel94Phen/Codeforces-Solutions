def get_count(curr, n, m):
    if curr in set([(1, 1), (n, m), (n, 1), (1, m)]):
        return 2
    elif curr[0] == 1 or curr[0] == n or curr[1] == m or curr[1] == 1:
        return 3
    return 4


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    c = set([1, n, m])
    print(min(get_count((x1, y1), n, m), get_count((x2, y2), n, m)))