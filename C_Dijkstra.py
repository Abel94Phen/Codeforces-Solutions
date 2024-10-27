import heapq
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

distances = {i : float('inf') for i in range(1, n + 1)}
distances[1] = 0
path = {1:-1}
heap = [(0, 1)]
heapq.heapify(heap)

while heap:
    distance, node = heapq.heappop(heap)
    for neighbor, cost in graph[node]:
        if distance + cost < distances[neighbor]:
            path[neighbor] = node
            distances[neighbor] = distance + cost
            heapq.heappush(heap, (distance + cost, neighbor))

curr = n
if curr not in path:
    print(-1)
else:
    stack = []
    while curr != -1:
        stack.append(curr)
        curr = path[curr]
    while stack:
        print(stack.pop(), end = ' ')