n, k = map(int, input().split())
path = list(map(int, input().split()))

max_length, length = 1, 1
for i in range(1, n):
    if path[i] == path[i - 1]:
        max_length = max(max_length, length)
        length = 1
    else:
        length += 1
print(max(max_length, length))