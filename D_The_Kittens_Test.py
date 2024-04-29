n = int(input())

parents = {i:i for i in range(1, n + 1)}
size = [1 for _ in range(n)]
groups = [[i] for i in range(1, n + 1)]

def find(child):
    if parents[child] == child:
        return child
    return find(parents[child])

def union(child_1, child_2):
    parent_1, parent_2 = find(child_1), find(child_2)
    if size[parent_1 - 1] < size[parent_2 - 1]:
        parents[parent_1] = parent_2
        size[parent_2 - 1] += size[parent_1 - 1]
        groups[parent_2 - 1].extend(groups[parent_1 - 1])
    else:
        parents[parent_2] = parent_1
        size[parent_1 - 1] += size[parent_2 - 1]
        groups[parent_1 - 1].extend(groups[parent_2 - 1])

for _ in range(n - 1):
    x, y = map(int, input().split())
    union(x, y)

for List in groups:
    if len(List) == n:
        print(*List)
        break