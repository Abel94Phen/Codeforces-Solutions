n, k = map(int, input().split())
array = list(map(float, input().split()))

def validate(x):
    increase, decrease = 0, 0

    for num in array:
        if num > x:
            diff = num - x
            increase += diff * (100 - k) / 100
        if num < x:
            decrease += x - num
    return increase >= decrease


left, right = 0, max(array) + 1
while left + 10**-10 < right:
    mid = (left + right) / 2
    if validate(mid):
        left = mid
    else:
        right = mid
print(left)
