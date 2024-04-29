n, m = map(int, input().split())
parents = {i:i for i in range(1, n + 1)}
rank = [1 for _ in range(n)]

def find(child):
    if parents[child] == child:
        return parents[child]
    return find(parents[child])

def union(node_1, node_2):
    parent_1, parent_2 = find(node_1), find(node_2)
    if parent_1 != parent_2:
        if rank[parent_1 - 1] > rank[parent_2 - 1]:
            parents[parent_2] = parent_1
            rank[parent_1 - 1] += 1
        else:
            parents[parent_1] = parent_2
            rank[parent_2 - 1] += 1

for _ in range(m):
    query = input().split()
    if query[0] == 'union':
        union(int(query[1]), int(query[2]))
    else:
        if find(int(query[1])) ==  find(int(query[2])):
            print("YES")
        else:
            print("NO")