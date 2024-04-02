t = int(input())
for _ in range(t):
    L = int(input())
    nums = list(map(int, input().split()))
    odds, evens = 0, 0
    for num in nums:
        if num%2:
            odds += 1
        else:
            evens += 1
    
    if odds != evens and odds + 1 != evens:
        print(-1)
    else:
        swaps = 0
        for i in range(L):
            if nums[i]%2 and i%2 == 0:
                swaps += 1
        print(swaps)