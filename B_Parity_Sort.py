t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    sortedArray = sorted(array)
    for i in range(n):
        if sortedArray[i]%2 != array[i]%2:
            print("NO")
            break
    else:
        print("YES")