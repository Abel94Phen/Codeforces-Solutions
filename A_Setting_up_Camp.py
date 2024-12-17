from math import ceil
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    result = a
    result += b//3
    if b%3:
        extra = 3 - b%3
        if extra > c:
            print(-1)
            continue
        else:
            c -= extra
            result += 1
    result += ceil(c/3)
    print(result)
