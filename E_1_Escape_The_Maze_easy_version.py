from collections import defaultdict
from collections import deque

t = int(input())
for _ in range(t):
    input()
    n, k = list(map(int, input().split()))
    freinds = list(map(int, input().split()))

    graph = defaultdict(list)

    for _ in range(n - 1):
        node1, node2 = list(map(int, input().split()))
        graph[node1].append(node2)
        graph[node2].append(node1)

    queue = deque()
    visited = set()

    for freind in freinds:
        queue.append(fr, fr)
        visited.add(fr)
    
    queue.append((1,1))
    visited.add(1)

    while queue:
        curr, root = queue.popleft()

        for neighbour in graph[curr]:
            if 
            queue.append((nbr, root))
           visited.add(neighbour)
