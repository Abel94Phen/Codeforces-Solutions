from collections import defaultdict
n = int(input())
numbers = list(map(int, input().split()))
visited = [False for _ in range(n)]


graph = defaultdict(list)

for i in range(1, n + 1):
    graph[i].append(numbers[i - 1])
    graph[numbers[i - 1]].append(i)

def dfs(node):
    stack = [node]
    while stack:
        node = stack.pop()
        visited[node - 1] = True
        for neighbour in graph[node]:
            if visited[neighbour - 1] == False:
                stack.append(neighbour)

count = 0
for i in range(n):
    if not visited[i]:
        dfs(i+1)
        count += 1
print(count)