shops = int(input())
prices = list(map(int, input().split()))
prices.sort()

def left_most(target):
    left, right = -1, shops
    while left < right - 1:
        mid = left + (right - left) // 2
        if prices[mid] <= target:
            left = mid
        else:
            right = mid
    return left + 1

days = int(input())
for _ in range(days):
    print(left_most(int(input())))