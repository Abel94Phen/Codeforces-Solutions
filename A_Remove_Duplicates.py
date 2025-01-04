n = int(input())
array = list(map(int, input().split()))
x = len(set(array))
seen = set()
result = [0 for _ in range(x)]
index = x - 1
for i in range(n - 1, -1, -1):
    if array[i] not in seen:
        result[index] = array[i]
        seen.add(array[i])
        index -= 1
print(x)
print(*result)