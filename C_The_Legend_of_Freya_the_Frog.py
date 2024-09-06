from math import ceil

t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())
    if ceil(x/k) <= ceil(y/k):
        print(2 * ceil(y/k))
    else:
        print(2 * ceil(x/k) - 1)