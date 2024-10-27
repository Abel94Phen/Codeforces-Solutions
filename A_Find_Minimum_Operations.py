from math import log
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
    else:
        x = int(log(n, k))
        result = 0
        decrement = k ** x
        while n:
            if decrement <= n:
                result += n//decrement
                n -= (n//decrement) * decrement
            else:
                decrement //= k
        print(result)
        