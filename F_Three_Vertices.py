from collections import defaultdict
from collections import deque
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


queue = deque([1])
visited = set([1])
last = None
while queue:
    for _ in range(len(queue)):
        last = queue.popleft()
        for neighbor in graph[last]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

a, b = last, last
queue = deque([b])
visited = set([b])
path = -1
while queue:
    for _ in range(len(queue)):
        b = queue.popleft()
        for neighbor in graph[b]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    path += 1

answer = [a, b]
for i in range(n):
    if i + 1 != a and i + 1 != b:
        answer.append(i + 1)
        break
print(path)
print(*answer)

