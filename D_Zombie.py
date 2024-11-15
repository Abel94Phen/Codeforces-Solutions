from collections import defaultdict
import heapq

n, m = map(int, input().split())
edge_count = [0 for _ in range(n + 1)]
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edge_count[u] += 1
    edge_count[v] += 1

start = -1
for i in range(n + 1):
    if edge_count[i] == 1:
        start = i

heap = [(0, start)]
distances = {i:float('inf') for i in range(1, n + 1)}
distances[start] = 0        

heapq.heapify(heap)
while heap:
    cost, curr = heapq.heappop(heap)
    for neighbor in graph[curr]:
        if cost + 1 < distances[neighbor]:
            distances[neighbor] = cost + 1
            heapq.heappush(heap, (cost + 1, neighbor))


candidate = max(distances.values())
start = -1
for i in range(1, n + 1):
    if distances[i] == candidate:
        start = i


heap = [(0, start)]
distances = {i:float('inf') for i in range(1, n + 1)}
distances[start] = 0        

heapq.heapify(heap)
while heap:
    cost, curr = heapq.heappop(heap)
    for neighbor in graph[curr]:
        if cost + 1 < distances[neighbor]:
            distances[neighbor] = cost + 1
            heapq.heappush(heap, (cost + 1, neighbor))
print(max(distances.values()))





