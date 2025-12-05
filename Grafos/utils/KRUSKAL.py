# ============================================================
# DSU (Disjoint Set Union) / Union-Find
# Sirve para:
#   - Manejar componentes que se van uniendo.
#   - Saber si dos nodos están en el mismo conjunto.
#   - Lo usamos en Kruskal para evitar ciclos.
# ============================================================

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
            return True   # se unieron dos componentes distintas
        return False       # ya estaban en el mismo conjunto

# ============================================================
# KRUSKAL: Árbol de expansión mínima (MST)
#
# PARA QUÉ SIRVE:
#   - Encontrar el costo mínimo para conectar TODOS los nodos
#     de un grafo NO DIRIGIDO con pesos.
#
# CÓMO SE USA:
#   1) Tener una lista de aristas: edges = [(costo, u, v), ...]
#      * u y v en 0-based (0..n-1)
#   2) Llamar:
#         total_cost, used_edges = kruskal(n, edges)
#   3) Si used_edges != n-1 -> grafo no conectable -> "IMPOSSIBLE"
#      Si used_edges == n-1 -> total_cost es el costo mínimo del MST
# ============================================================

def kruskal(n, edges):
    # edges: lista de tuplas (costo, u, v)
    edges.sort()          # ordenar por costo creciente
    dsu = DSU(n)
    total_cost = 0
    used_edges = 0

    for cost, u, v in edges:
        if dsu.union(u, v):           # une si estaban en componentes distintas
            total_cost += cost
            used_edges += 1

    return total_cost, used_edges