t = int(input())
for _ in  range(t):
    n = int(input())
    array = list(map(int, input().split()))

    sortedArray = sorted(array)
    inposition = 0
    for i in range(n):
        if array[i] == sortedArray[i]:
            inposition += 1

    if inposition == n:
        print(0)
    elif array[0] == sortedArray[0] or array[-1] == sortedArray[-1]:
        print(1)
    else:
        print(2)
