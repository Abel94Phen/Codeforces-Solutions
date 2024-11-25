n = int(input())
heights = list(map(int, input().split()))
index_1, index_2 = 1, 2
curr = abs(heights[0] - heights[1])
for i in range(n + 1):
    diff = abs(heights[i%n] - heights[(i + 1)%n])
    if diff < curr:
        curr = diff
        index_1, index_2 = i%n + 1, (i + 1)%n + 1
print(index_1, index_2)