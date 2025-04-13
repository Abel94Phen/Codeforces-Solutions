from collections import Counter
t = int(input())
for _ in range(t):
    n, left_len, right_len = map(int, input().split())
    arr = list(map(int, input().split()))
    left, right = arr[:left_len], arr[left_len:]
    left.sort()
    right.sort()
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] == right[r]:
            left[l], right[r] = None, None
            l += 1
            r += 1
        elif left[l] < right[r]:
            l += 1
        else:
            r += 1
    left, right = [num for num in left if num], [num for num in right if num]
    left_count, right_count = Counter(left), Counter(right)
    left_portion, right_portion = [], []
    for number, count in left_count.items():
        left_portion.append([number, count])
    for number, count in right_count.items():
        right_portion.append([number, count])
    
    left_portion.sort(key = lambda x : x[1])
    right_portion.sort(key = lambda x : x[1])
    result = 0
    i, j = 0, 0
    while i < len(left_portion) and j < len(right_portion):
        if left_portion[i][1] == right_portion[j][1]:
            result += left_portion[i][1]
            i += 1
            j += 1
        elif left_portion[i][1] < right_portion[j][1]:
            result += left_portion[i][1]
            right_portion[j][1] -= left_portion[i][1]
            i += 1
        else:
            result += right_portion[j][1]
            left_portion[i][1] -= right_portion[j][1]
            j += 1
    extras = 0
    while i < len(left_portion):
        result += left_portion[i][1] // 2
        extras += left_portion[i][1] % 2
        i += 1
    while j < len(right_portion):
        result += right_portion[j][1] // 2
        extras += right_portion[j][1] % 2
        j += 1
    print(result + extras)
 