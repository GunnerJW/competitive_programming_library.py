class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.disjoint_sets = n

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def is_same_set(self, x, y):
        return self.find_parent(x) == self.find_parent(y)

    def unite(self, x, y):
        if self.is_same_set(x, y):
            return
        p_x = self.find_parent(x)
        p_y = self.find_parent(y)
        if self.rank[p_x] > self.rank[p_y]:
            self.parent[p_y] = p_x
        else:
            self.parent[p_x] = p_y
            if self.rank[p_x] == self.rank[p_y]:
                self.rank[p_y] += 1
        self.disjoint_sets -= 1
