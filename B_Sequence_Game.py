t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    
    result = [array[0]]
    for i in range(1, length):
        if array[i] >= result[-1]:
            result.append(array[i])
        else:
            result.extend([array[i], array[i]])
    print(len(result))
    print(*result)