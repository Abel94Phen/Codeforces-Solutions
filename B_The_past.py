n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

if a[0] == 0:
    a[0] = b.pop()

def leftMost(target):
    left, right = -1, len(b)
    while left + 1 < right:
        mid = (left + right) // 2
        if b[mid] < target:
            left = mid
        else:
            right = mid
    return left

for i in range(n - 1):
    if a[i + 1] == 0:
        index = leftMost(a[i])
        if index == -1:
            a[i + 1] = b.pop()
        else:
            print("Yes")
            break
    else:
        if a[i] > a[i + 1]:
            print("Yes")
            break
else:
    print("No")
