t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    increment = a + b + c
    days = 3 * (n // increment)
    n %= increment
    if n <= 0:
        print(days)
    else:
        n -= a
        days += 1
        if n <= 0:
            print(days)
            continue
        n -= b
        days += 1
        if n <= 0:
            print(days)
            continue
        n -= c
        days += 1
        if n <= 0:
            print(days)
            continue