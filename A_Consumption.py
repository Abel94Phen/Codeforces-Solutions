n = int(input())
remaining = list(map(int, input().split()))
cans = list(map(int, input().split()))

total = sum(remaining)
cans.sort()

if cans[-1] + cans[-2] >= total:
    print("YES")
else:
    print("NO")