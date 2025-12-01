# ================================================
# DSU / Union-Find
# Uso:
#   dsu = DSU(n)
#   dsu.union(a, b)        # unir conjuntos
#   dsu.find(x)            # obtener representante
#   dsu.find(a) == dsu.find(b)  -> conectados
# ================================================

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            # union by size
            if self.sz[a] < self.sz[b]:
                a, b = b, a
            self.parent[b] = a
            self.sz[a] += self.sz[b]

    def size(self, x):
        return self.sz[self.find(x)]
