from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    x = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            x = max(x, ceil((nums[i] + nums[i + 1]) / 2))    
    for i, num in enumerate(nums):
        nums[i] = abs(num - x)
    flag = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            flag = False
            break
    if flag:
        print(x)
    else:
        print(-1)