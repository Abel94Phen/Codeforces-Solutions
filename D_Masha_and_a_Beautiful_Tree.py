def merge_sort(nums, left, right):
    if left == right:
        return 0
    
    mid = (left + right) // 2
    left_half = nums[left : mid + 1]
    right_half = nums[mid + 1 : right + 1]
    
    max_left, max_right = max(left_half), max(right_half)
    moves = 0
    if max_left > max_right:
        nums[mid + 1 : right + 1] = left_half
        nums[left : mid + 1] = right_half
        moves += 1
    return merge_sort(nums, left, mid) + merge_sort(nums, mid + 1, right) + moves
    
    
t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    answer = merge_sort(array, 0, length - 1)
    if array == sorted(array):
        print(answer)
    else:
        print(-1)