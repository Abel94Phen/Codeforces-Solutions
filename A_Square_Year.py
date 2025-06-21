def squareRoot(number):
    left, right = 0, number
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < number:
            left = mid + 1
        else:
            right = mid - 1
    return left

t = int(input())
for _ in range(t):
    target = int(input())
    candidate = squareRoot(target)
    if candidate * candidate == target:
        print(candidate, 0)
    else:
        print(-1)