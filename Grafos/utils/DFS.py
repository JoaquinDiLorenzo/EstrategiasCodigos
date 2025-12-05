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

def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


# Variante: DFS que devuelve tamaño de la componente de node
def dfs_count(node, graph, visited):
    visited[node] = True
    total_nodes = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            total_nodes += dfs_count(neighbor, graph, visited)
    return total_nodes
