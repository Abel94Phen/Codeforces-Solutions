n, k = map(int, input().split())
array = list(map(int, input().split()))
indices = [1]
seen = set([array[0]])
for i in range(1, n):
    if array[i] not in seen:
        indices.append(i + 1)
        seen.add(array[i])
if len(indices) < k:
    print("NO")
else:
    print("YES")
    print(*indices[:k])