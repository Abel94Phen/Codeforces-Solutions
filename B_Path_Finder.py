from collections import defaultdict
from collections import deque

nodes = int(input())
graph = defaultdict(list)

for _ in range(nodes - 1):
    u,v,c = map(int, input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

queue = deque([(0,0)])
visited = set()
distances = [0]

while queue:
    length = len(queue)
    for _ in range(length):
        node, d = queue.popleft()
        visited.add(node)
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, (d + cost)))
                distances.append(d + cost)

print(max(distances))