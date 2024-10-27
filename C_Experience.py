class UnionFind:
    def __init__(self, n):
        self.parents = {i:i for i in range(1, n + 1)}
        self.size = [1 for _ in range(n + 1)]
        self.excess = [0 for i in range(n + 1)]
        self.experience = [0 for i in range(n + 1)]

    def find(self, child):
        if child == self.parents[child]:
            return child
        return self.find(self.parents[child])
    
    def get(self, child):
        if child == self.parents[child]:
            return self.experience[child]
        return (self.experience[child] - self.excess[child]) + self.get(self.parents[child])
    
    def union(self, child_1, child_2):
        parent_1, parent_2 = self.find(child_1), self.find(child_2)
        if parent_1 != parent_2:
            if self.size[parent_1] < self.size[parent_2]:
                parent_1, parent_2 = parent_2, parent_1
            
            self.parents[parent_2] = parent_1
            self.size[parent_1] += self.size[parent_2]
            self.excess[parent_2] = self.experience[parent_1]

    def add(self, child, points):
        child = self.find(child)
        self.experience[child] += points

        
n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    query = input().split()
    if query[0] == 'join':
        uf.union(int(query[1]), int(query[2]))
    elif query[0] == 'add':
        uf.add(int(query[1]), int(query[2]))
    else:
        print(uf.get(int(query[1])))
