t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    left = 0
    maximum_length, curr_length = 0, 0
    for right in range(length):
        if array[right] == 0:
            curr_length += 1
        else:
            maximum_length = max(maximum_length, curr_length)       
            curr_length = 0
        
    print(max(maximum_length, curr_length))