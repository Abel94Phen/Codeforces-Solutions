t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(n):
        array[i] = array[i]%2
    left, right = 0, 0
    result, count = 0, 0
    while right < n:
        if array[right] == array[left]:
            count += 1
        else:
            if count:
                result += count - 1
                count = 1
            left = right
        right += 1
    if count:
        result += count - 1
        count = 1
    print(result)
