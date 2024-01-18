length, sub_sum = list(map(int, input().split()))
array = list(map(int, input().split()))

sum = 0
l = 0
count = 0
for r in range(length):
    sum += array[r]
    while sum >= sub_sum:
        count += 1
        sum -= array[l]
        l += 1
print(count)    