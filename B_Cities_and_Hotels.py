n, d = map(int, input().split())
array = list(map(int, input().split()))
array = [float("-inf")] + array + [float("inf")]

count = 0
for i in range(1, n + 1):
    new_left, new_right = array[i] - d, array[i] + d
    
    if abs(new_left - array[i - 1]) > d:
        count += 1
    
    if abs(new_right - array[i + 1]) >= d:
        count += 1

print(count)

