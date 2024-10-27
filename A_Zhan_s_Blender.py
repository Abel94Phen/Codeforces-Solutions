from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    print(ceil(n / (min(x, y))))