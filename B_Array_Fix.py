t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    i = length - 1
    to_sort = [array[-1]]
    while i > 0:
        if array[i - 1] > to_sort[-1]:
            x, y = array[i - 1] // 10, array[i - 1] % 10
            to_sort.append(y)            
            to_sort.append(x)
        else:
            to_sort.append(array[i - 1])            
        i -= 1

    
    if to_sort == sorted(to_sort, reverse = True):
        print("YES")
    else:
        print("NO")