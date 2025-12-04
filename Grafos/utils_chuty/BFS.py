# ===================================================================
# BFS (Breadth-First Search)
#
# PARA QUÉ SIRVE:
#   - Encontrar la distancia MÍNIMA en cantidad de aristas.
#   - Saber cuántos pasos hay desde un nodo a otro.
#
# CUÁNDO USARLO:
#   - Grafos SIN peso (todas las aristas valen 1).
#   - Cuando querés distancia mínima PERO NO necesitás el camino.
#
# CÓMO USARLO:
#   1) Construí el grafo:
#         graph = [[] for _ in range(n)]
#         graph[a].append(b)
#         graph[b].append(a)
#   2) Llamá:
#         dist = bfs(start, graph, n)
#   3) dist[v] = distancia mínima desde start a v
# ===================================================================

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()
        for to in graph[v]:
            if dist[to] == -1:      # no visitado aún
                dist[to] = dist[v] + 1
                q.append(to)

    return dist

# ===================================================================
# BFS + reconstrucción del CAMINO MÍNIMO
#
# PARA QUÉ SIRVE:
#   - Encontrar el camino MÍNIMO entre start y end.
#   - Útil en "Message Route" o cualquier ejercicio de ruta mínima.
#
# CUÁNDO USARLO:
#   - Grafos SIN peso.
#   - Cuando necesitás imprimir el camino (1 4 5 ...).
#
# CÓMO USARLO:
#   1) Construí el grafo:
#         graph = [[] for _ in range(n)]
#         graph[a].append(b)
#         graph[b].append(a)
#   2) Llamá:
#         path = bfs_path(start, end, graph, n)
#   3) Si path es None → no hay ruta
#      Si existe → path = lista de nodos (0-based)
#         Para imprimir 1-based:
#             print(*[x+1 for x in path])
# ===================================================================

from collections import deque

def bfs_path(start, end, graph, n):
    dist = [-1] * n
    parent = [-1] * n
    dist[start] = 0

    q = deque([start])

    while q:
        v = q.popleft()
        for to in graph[v]:
            if dist[to] == -1:      # no visitado aún
                dist[to] = dist[v] + 1
                parent[to] = v
                q.append(to)

    if dist[end] == -1:
        return None

    # reconstrucción del camino: end → start usando parent[]
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path
