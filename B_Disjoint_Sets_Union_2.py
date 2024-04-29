n, m = map(int, input().split())

parents = {i:i for i in range(1, n + 1)}
size = [1 for _ in range(n)]

minimal = [i for i in range(1, n + 1)]
maximal = [i for i in range(1, n + 1)]

def find(child):
    if parents[child] == child:
        return child
    return find(parents[child])

def union(node_1, node_2):
    parent_1, parent_2 = find(node_1), find(node_2)

    if parent_1 != parent_2:
        if size[parent_1 - 1] > size[parent_2 - 1]:
            parents[parent_2] = parent_1
            size[parent_1 - 1] += size[parent_2 - 1]
            minimal[parent_1 - 1] = min(minimal[parent_1 - 1], minimal[parent_2 - 1])
            maximal[parent_1 - 1] = max(maximal[parent_1 - 1], maximal[parent_2 - 1])
        else:
            parents[parent_1] = parent_2
            size[parent_2 - 1] += size[parent_1 - 1]
            minimal[parent_2 - 1] = min(minimal[parent_1 - 1], minimal[parent_2 - 1])
            maximal[parent_2 - 1] = max(maximal[parent_1 - 1], maximal[parent_2 - 1])


for _ in range(m):
    query = input().split()
    if query[0] == 'union':
        union(int(query[1]), int(query[2]))
    else:
        node = find(int(query[1]))

        print(minimal[node - 1], maximal[node - 1], size[node - 1])    