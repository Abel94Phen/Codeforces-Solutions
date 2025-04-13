n, t, c = map(int, input().split())
array = list(map(int, input().split()))
left = 0
invalids = 0
result = 0
for i in range(c - 1):
    if array[i] > t:
        invalids += 1
for right in range(c - 1, n):
    if array[right] > t:
        invalids += 1
    if invalids == 0:
        result += 1
    if array[left] > t:
        invalids -= 1
    left += 1
print(result)