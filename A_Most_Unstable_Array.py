t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if n - 1 == 0:
        print(0)
    elif n - 1 > 1:
        print(2 * m)
    else:
        print(m)