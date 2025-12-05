# ============================================================
# KRUSKAL: Árbol de expansión mínima (MST)
#
# PARA QUÉ SIRVE:
#   - Encontrar el costo mínimo para conectar TODOS los nodos
#     de un grafo NO DIRIGIDO con pesos.
#
# CÓMO SE USA:
#   1) Tener una lista de aristas: 
    #     edges = []
    # for _ in range(m):
    #     a, b, c = map(int, input().split())
    #     a -= 1   # pasar a 0-based
    #     b -= 1
    #     edges.append((c,a,b)) -> VA EL PESO PRIMERO

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