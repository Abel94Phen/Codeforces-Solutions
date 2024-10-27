class UnionFind:
    def __init__(self, n):
        self.parents = {i:i for i in range(1, n + 1)}
        self.size = [1 for _ in range(n + 1)]
        self.next_index = [i + 1 for i in range(n + 1)]

    def find(self, child):
        while child != self.parents[child]:
            self.parents[child] = self.parents[self.parents[child]]
            child = self.parents[child]
        return child    
   
    def union(self, child_1, child_2):
        parent_1, parent_2 = self.find(child_1), self.find(child_2)
        if parent_1 != parent_2:
            if self.size[parent_1] < self.size[parent_2]:
                parent_1, parent_2 = parent_2, parent_1
            self.parents[parent_2] = parent_1
            self.size[parent_1] += self.size[parent_2]

    def rangeUnion(self, child_1, child_2):
        curr = child_1
        while curr < child_2:
            next = self.next_index[curr]
            self.next_index[curr] = self.next_index[child_2]
            self.union(curr, child_2)
            curr = next

    def isConnected(self, child_1, child_2):
        return self.find(child_1) == self.find(child_2)

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    type, x, y = map(int, input().split())
    if type == 1:
        uf.union(x, y)
    elif type == 2:
        uf.rangeUnion(x, y)
    else:
        print("YES") if uf.isConnected(x, y) else print("NO")
