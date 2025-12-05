# ===================================================================
# DFS (Depth-First Search)
#
# PARA QUÉ SIRVE:
#   - Recorrer un grafo completamente.
#   - Encontrar componentes conexas.
#   - Contar nodos en una componente.
#   - Detectar ciclos (con más lógica).
#
# CUÁNDO USARLO:
#   - Cuando NECESITÁS RECORRER todo el grafo.
#   - Cuando NO necesitás caminos mínimos.
#
# CÓMO USARLO:
#   1) Construí el grafo:
#         graph = [[] for _ in range(n)]
#         graph[a].append(b)
#         graph[b].append(a)
#   2) Creá visited:
#         visited = [False] * n
#   3) Llamá:
#         dfs(start, graph, visited)
# ===================================================================

def dfs(v, graph, visited):
    visited[v] = True
    for to in graph[v]:
        if not visited[to]:
            dfs(to, graph, visited)


# Variante: DFS que devuelve tamaño de la componente de v
def dfs_count(v, graph, visited):
    visited[v] = True
    total = 1
    for to in graph[v]:
        if not visited[to]:
            total += dfs_count(to, graph, visited)
    return total
