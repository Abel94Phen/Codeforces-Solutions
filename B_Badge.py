n = int(input())
array = list(map(int, input().split()))
result = []
for i in range(n):
    seen = set([i + 1])
    curr = array[i]
    while curr not in seen:
        seen.add(curr)
        curr = array[curr - 1]
    result.append(curr)
print(*result)