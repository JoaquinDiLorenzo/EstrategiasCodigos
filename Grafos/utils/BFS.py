
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
#      (usar 0-based: 0..n-1)
#   2) Llamá:
#         dist = bfs(start, graph, n)
#   3) dist[v] = distancia mínima desde start a v
# ===================================================================

def bfs(start_node, graph, node_count):
    distance = [-1] * node_count
    distance[start_node] = 0
    queue = deque([start_node])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:      # no visitado aún
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return distance


# ===================================================================
# BFS + reconstrucción del CAMINO MÍNIMO
#
# PARA QUÉ SIRVE:
#   - Encontrar el camino MÍNIMO entre start y end.
#   - Útil en "Message Route" o cualquier ejercicio de ruta mínima
#     que pida imprimir el camino.
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

def bfs_path(start_node, end_node, graph, node_count):
    distance = [-1] * node_count
    parent = [-1] * node_count
    distance[start_node] = 0

    queue = deque([start_node])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:      # no visitado aún
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    if distance[end_node] == -1:
        return None

    # reconstrucción del camino: end_node → start_node usando parent[]
    path = []
    node = end_node
    while node != -1:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path