t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    pivot = array.index(1)
    left, right = pivot - 1, pivot + 1
    result = ['1']
    total = 1
    while left > -1 and right < n:
        if array[left] < array[right]:
            total += array[left]
            left -= 1
        else:
            total += array[right]
            right += 1
        length = len(result) + 1
        if total == (length + 1) * length // 2:
            result.append('1')
        else:
            result.append('0')
    while left > -1:
        total += array[left]
        left -= 1
        length = len(result) + 1
        if total == (length + 1) * length // 2:
            result.append('1')
        else:
            result.append('0')
    while right < n:
        total += array[right]
        right += 1
        length = len(result) + 1
        if total == (length + 1) * length // 2:
            result.append('1')
        else:
            result.append('0')
    print("".join(result))
