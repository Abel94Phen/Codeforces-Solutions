t = int(input())
while t > 0:
    input()
    nums = list(map(int, input().split()))
    odds, evens = 0, 0
    for num in nums:
        if num%2:
            odds += 1
        else:
            evens += 1
    if odds == evens:
        print("Yes")
    else:
        print("No")
    t -= 1