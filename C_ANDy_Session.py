t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    curr = (1<<31) - 1
    for num in nums:
        curr &= num
    
    
    if k == 0:
        print(curr)
        continue
    
    for i in range(30, -1, -1):
        count = 0
        for num in nums:
            if not (num & (1<<i)):
                count += 1
        if count and count <= k:
            curr = (1 << i) | curr
            k -= count
            
    
    print(curr)