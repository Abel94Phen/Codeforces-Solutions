t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    diff = r - l

    left, right = 1, 89445
    while left < right:
        mid = (left + right) // 2
        if (mid**2 + mid) // 2 <= diff:
            left = mid + 1
        else:
            right = mid
    
    print(right)