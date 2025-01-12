from collections import defaultdict
from collections import deque


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = [0 for _ in range(3)]

queue = deque([1])
visited = set([1])
a = 0
while queue:
    for _ in range(len(queue)):
        a = queue.popleft()
        for neighbor in graph[a]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

answer[0] = a
b = a
queue = deque([b])
parent = {b : - 1}
while queue:
    for _ in range(len(queue)):
        b = queue.popleft()
        for neighbor in graph[b]:
            if neighbor not in parent:
                parent[neighbor] = b
                queue.append(neighbor)

answer[1] = b
curr = answer[1]
path = []
while curr != -1:
    path.append(curr)
    curr = parent[curr]
if len(path) == n:
    for i in range(n):
        if i + 1 != answer[0] and i + 1 != answer[1]:
            answer[2] = i + 1
    print(n - 1)
    print(*answer)
else:
    last = -1
    queue = deque(path)
    visited = set(path)
    depth = -1
    while queue:
        for _ in range(len(queue)):
            last = queue.popleft()
            for neighbor in graph[last]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        depth += 1

    answer[2] = last
    print(len(path) + depth - 1)
    print(*answer)

