n, k = map(int, input().split())
array = list(map(int, input().split()))
left = 0
total = 0
result = sum(array)
index = 1
for right in range(n):
    total += array[right]
    if right - left + 1 == k:
        if total < result:
            result = total
            index = left + 1
        total -= array[left]
        left += 1
print(index)