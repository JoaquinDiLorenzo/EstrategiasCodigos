# ================================================================
# DSU (Disjoint Set Union) / Union-Find
#
# PARA QUÉ SIRVE:
#   - Maneja GRUPOS de nodos que se van uniendo con el tiempo.
#   - Responde: "¿Estos dos nodos están en el MISMO grupo?"
#   - No sirve para obtener caminos. Solo sirve para conectividad.
#
# CUÁNDO USARLO:
#   - Muchos "UNIR a b" y "PREGUNTAR si a y b están conectados".
#   - Kruskal (Minimum Spanning Tree).
#
# CÓMO USARLO:
#   dsu = DSU(n)                 # inicializar con n nodos
#   dsu.union(a, b)              # unir los conjuntos donde están a y b
#   dsu.find(x)                  # obtener el representante del grupo
#   dsu.find(a) == dsu.find(b)   # True si están en el mismo grupo
#   dsu.size(x)                  # tamaño del grupo de x
# ================================================================

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.sz[a] < self.sz[b]:
                a, b = b, a
            self.parent[b] = a
            self.sz[a] += self.sz[b]

    def size(self, x):
        return self.sz[self.find(x)]