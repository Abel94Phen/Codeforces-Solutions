length, sub_sum = list(map(int, input().split()))
array = list(map(int, input().split()))

sum = 0
l = 0
Len = float('inf')
for r in range(length):
    sum += array[r]
    while sum >= sub_sum:
        sum -= array[l]
        Len = min(Len, r - l + 1)
        l += 1

if Len == float('inf'):
    print(-1)
else:
    print(Len)    