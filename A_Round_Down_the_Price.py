from math import log10
t = int(input())
for _ in range(t):
    m = int(input())
    power = int(log10(m))
    target = 10**power
    print(m - target)