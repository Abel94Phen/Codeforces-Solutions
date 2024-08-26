t = int(input())

for _ in range(t):
    array = list(map(int, input().split()))
    left, right = 1, 5
    target = array[-1] - array[0]
    result = [array[0]]
    while left < right:
        if array[left] + array[right] == target:
            result.extend([array[left], array[right]])
            break
        elif array[left] + array[right] > target:
            right -= 1
        else:
            left += 1
    print(*result)
