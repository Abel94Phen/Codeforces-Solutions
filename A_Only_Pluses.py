import heapq

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    
    heapq.heapify(nums)
    
    steps = 5
    while steps:
        heapq.heappush(nums, heapq.heappop(nums) + 1)
        steps -= 1
    
    print(nums[0] * nums[1] * nums[2])