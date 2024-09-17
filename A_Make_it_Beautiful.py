t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    result = []
    left, right = 0, n - 1
    while left < right:
        result.append(array[left])
        result.append(array[right])
        left += 1
        right -= 1

    if left == right:
        result.append(array[left])

    total = 0
    for i in range(n):
        if result[i] == total:
            print("NO")
            break
        total += result[i]
    else:
        print("YES")
        print(*result)