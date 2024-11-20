t = int(input())
for _ in range(t):
    k = int(input())
    array = list(map(int, input().split()))
    array.sort()
    left, right = 0, k - 1
    while left < right:
        curr = array[left] * array[right]
        if curr == k - 2:
            print(array[left], array[right])
            break
        elif curr > k - 2:
            right -= 1
        else:
            left += 1
