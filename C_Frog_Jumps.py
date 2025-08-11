t = int(input())
for _ in range(t):
    path = input()
    result  = 0
    left = -1
    for right in range(len(path)):
        if path[right] == 'R':
            result = max(result, right - left)
            left = right
    
    result = max(result, right - left + 1)
    print(result)