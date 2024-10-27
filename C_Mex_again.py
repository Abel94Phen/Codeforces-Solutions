n = int(input())
array = list(map(int,input().split()))
array.sort()
curr = 1
for i in range(n):
    if array[i] >= curr:
        curr += 1
print(curr)