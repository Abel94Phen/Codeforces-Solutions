t = int(input())
while t > 0:
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[-1] + nums[-2] >= 10:
        print("YES")
    else:
        print("NO")
    t -= 1