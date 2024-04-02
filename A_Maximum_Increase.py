length = int(input())
nums = list(map(int, input().split()))

max_len = 1
left, right = 0, 1
while right < length:
    if nums[right] <= nums[right - 1]:
        left = right
    max_len = max(max_len, right - left + 1)
    right += 1
print(max_len)