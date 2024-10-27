import heapq
from collections import defaultdict

def dijkistra(graph, n, src):
    distances = {i : float('inf') for i in range(1, n + 1)}
    distances[src] = 0
    heap = [(0, src)]
    heapq.heapify(heap)
    
    while heap:
        cost, node = heapq.heappop(heap)
        for neighbor in graph[node]:
            if cost + 1 < distances[neighbor]:
                distances[neighbor] = cost + 1
                heapq.heappush(heap, (cost + 1, neighbor))
    return distances

n, m = map(int, input().split())
graph_railway = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph_railway[u].add(v)
    graph_railway[v].add(u)

graph_road = defaultdict(set)
for node, reaches in graph_railway.items():
    for i in range(n):
        if i + 1 not in reaches and i + 1 != node:
            graph_road[i + 1].add(node)
            graph_road[node].add(i + 1)

bus = dijkistra(graph_road, n, 1)[n]
train = dijkistra(graph_railway, n, 1)[n]

if bus == float('inf') or train == float('inf'):
    print(-1)
else:
    print(max(bus, train))