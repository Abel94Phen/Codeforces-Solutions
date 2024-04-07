from collections import defaultdict
v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

degrees = [0 for _ in range(v)]
for node in graph:
    degrees[node - 1] += len(graph[node])

if degrees.count(2) == v - 2 and degrees.count(1) == 2:
    print("bus topology")
elif degrees.count(1) == v - 1 and degrees.count(e) == 1:
    print("star topology")
elif degrees.count(2) == e:
    print("ring topology")
else:
    print("unknown topology")