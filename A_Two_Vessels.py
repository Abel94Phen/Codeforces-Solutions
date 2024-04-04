from math import ceil
t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    print(ceil(abs(a - (a + b)/2)/c))