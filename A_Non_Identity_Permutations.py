t = int(input())

for _ in range(t):
    length = int(input())
    array = [i for i in range(1, length + 1)]

    left, right = 0, length - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    if length > 1 and length%2:
        array[left], array[left + 1] = array[left + 1], array[left]

    print(*array)