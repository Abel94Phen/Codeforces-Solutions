from math import ceil

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(k - 1, 0, -1):
        array[i] -= array[i - 1]
    
    for i in range(k - 1, 1, -1):
        if array[i - 1] > array[i]:
            print("No")
            break
    else:
        if k == 1 or ceil(array[0] / (n - k + 1)) <= array[1]:
            print("Yes")
        else:
            print("No")