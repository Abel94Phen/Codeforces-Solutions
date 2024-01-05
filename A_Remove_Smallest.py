t = int(input())
while t > 0:
    array_len = int(input())
    array = list(map(int, input().split()))
    array.sort()
    i,count = 1,0
    while i < array_len:
        if array[i] > array[i-1] and array[i] - array[i-1] == 1:
            count += 1
        elif array[i] == array[i-1]:
            count += 1
        i += 1
    if count == array_len - 1:
        print("YES")
    else:
        print("NO")
    t -= 1