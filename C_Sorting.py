n = int(input())
array = list(map(int, input().split()))
sortedArray = sorted(array)
left, right = 0, n - 1

while left < right and array[left] == sortedArray[left]:
    left += 1

while left < right and array[right] == sortedArray[right]:
    right -= 1

if left == n - 1:
    print("yes")
    print(1, 1)
else:
    l, r = left, right
    while left <= r and array[left] == sortedArray[right]:
        left += 1
        right -= 1
    
    if left > r:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")