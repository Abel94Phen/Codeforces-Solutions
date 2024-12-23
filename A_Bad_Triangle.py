t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    if array[-1] >= array[0] + array[1]:
        print(1, 2, n)
    else:
        print(-1)