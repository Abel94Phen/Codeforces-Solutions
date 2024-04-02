t = int(input())
while t > 0:
    input()
    nums = list(map(int, input().split()))
    odds = 0
    for num in nums:
        if num % 2:
            odds += 1
    if odds%2:
        print("NO")
    else:
        print("YES")
    t -= 1