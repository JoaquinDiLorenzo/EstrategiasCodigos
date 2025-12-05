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
#   dsu = DSU(n)                   # inicializar con n nodos (0..n-1)
#   dsu.union(a, b)                # unir los conjuntos donde están a y b
#   dsu.find(x)                    # obtener el representante del grupo
#   dsu.find(a) == dsu.find(b)     # True si están en el mismo grupo
#   dsu.size(x)                    # tamaño del grupo de x
# ================================================================

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size_array = [1] * n

    def find(self, x):
        # encuentra el representante del conjunto de x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        # une los conjuntos de a y b, devuelve True si se unieron
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False  # ya estaban unidos

        # unión por tamaño
        if self.size_array[root_a] < self.size_array[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size_array[root_a] += self.size_array[root_b]
        return True

    def size(self, x):
        return self.size_array[self.find(x)]