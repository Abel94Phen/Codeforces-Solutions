length = int(input())
array = list(map(int, input().split()))

array.sort()

count = 0
waiting = 0

for i in range(length):
    if array[i] >= waiting:
        count += 1

    else:
        array[i] = 0
    
    waiting += array[i]

print(count)
    
