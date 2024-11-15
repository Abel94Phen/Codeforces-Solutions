from collections import defaultdict
from collections import deque
n = int(input())
graph = defaultdict(list)
queue = deque()
for i in range(n):
    u, v = i + 1, int(input())
    if v == -1:
        queue.append(u)
    else:
        graph[v].append(u)
groups = 0
while queue:
    for _ in range(len(queue)):
        curr = queue.popleft()
        for neighbor in graph[curr]:
            queue.append(neighbor)
    groups += 1
print(groups)