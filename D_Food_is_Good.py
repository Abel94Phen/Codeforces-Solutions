t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    x = sum(array)

    max_sum1 = 0
    local_sum = 0
    
    for i in range(length - 1):
        local_sum = max(local_sum + array[i], array[i])
        max_sum1 = max(max_sum1, local_sum)
    
    max_sum2 = 0
    local_sum = 0
    
    for i in range(1, length):
        local_sum = max(local_sum + array[i], array[i])
        max_sum2 = max(max_sum2, local_sum)

    max_sum = max(max_sum1, max_sum2)

    print("YES") if sum(array) > max_sum else print("NO")