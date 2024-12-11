from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    inplace = 0
    for i in range(n):
        if array[i] == i + 1:
            inplace += 1
    print(int(ceil(inplace/2)))