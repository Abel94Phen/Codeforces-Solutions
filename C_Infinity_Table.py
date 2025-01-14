t = int(input())
for _ in range(t):
    k = int(input())
    d = 1
    while (d + 1) * (d + 1) <= k:
        d += 1
    k -= d * d
    if k == 0:
        print(d, 1)
    elif k <= d + 1:
        print(k, d + 1)
    else:
        excess = k - d - 1
        print(d + 1, d + 1 - excess)