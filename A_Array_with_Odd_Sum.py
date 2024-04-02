t = int(input())
for _ in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
    odds, evens = 0, 0
    for num in nums:
        if num%2:
            odds += 1
        else:
            evens += 1
    if odds%2:
        print("YES")
    elif not odds%2 and odds > 1 and evens >= 1:
        print("YES")
    else:
        print("NO")