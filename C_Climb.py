n, m = map(int, input().split())
if n < m:
    print(-1)
else:
    steps = n // 2 + int(n%2 == 1)
    if steps%m:
        steps += m - steps%m
    print(steps)
