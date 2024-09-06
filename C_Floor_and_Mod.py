from math import ceil, sqrt


t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    result = 0
    for i in range(1, ceil(sqrt(x))):
        result += max(0,min(y,x//i-1)-i)
        
    print(result)