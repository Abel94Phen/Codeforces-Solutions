t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    array.sort()

    if array[0] != 1:
        print("NO")
    
    else:
        prefix_sum = 1

        flag = True
        for i in range(1, length):
            if array[i] > prefix_sum:
                flag = not flag
                break
            prefix_sum += array[i]
        
        print("YES") if flag else print("NO")