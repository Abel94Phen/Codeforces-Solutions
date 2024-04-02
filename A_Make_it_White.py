t = int(input())
for _ in range(t):
    length = int(input())
    block = input()
    left, right = 0, length - 1
    
    while left < length:
        if block[left] == 'B':
            break
        left += 1
    
    while right > -1:
        if block[right] == 'B':
            break
        right -= 1
        
    if left > right:
        print(0)
    else:
        print(right - left + 1)