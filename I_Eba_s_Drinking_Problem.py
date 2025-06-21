n = int(input())
array = list(map(int, input().split()))
array.sort()
q = int(input())
for _ in range(q):
    target = int(input())
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    print(right + 1)