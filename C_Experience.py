class UnionFind:
    def __init__(self, n):
        self.parents = {i:i for i in range(1, n + 1)}
        self.size = {i:1 for i in range(1, n + 1)}
        # self.experience = {i:0 for i in range(1, n + 1)}

    def find(self, child):
        while child != self.parents[child]:
            child = self.parents[child]
        return child
    
    def union(self, child_1, child_2):
        parent_1, parent_2 = self.find(child_1), self.find(child_2)
        if parent_1 != parent_2:
            if self.size[parent_1] >= self.size[parent_2]:
                self.parents[parent_2] = parent_1
                self.size[parent_1] += self.size[parent_2]
            else:
                self.parents[parent_1] = parent_2
                self.size[parent_2] += self.size[parent_1]