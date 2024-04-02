length = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0

i = 0
for j in range(1, length):
    if array[i] < array[j]:
        count += 1
        i += 1

print(count)
