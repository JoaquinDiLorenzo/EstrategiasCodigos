# ============================================================
# PUNTOS DE ARTICULACIÓN (Necessary Cities)
#
# PARA QUÉ SIRVE:
#   - Encontrar TODOS los nodos que, si los removés (y sus aristas),
#     hacen que el grafo quede desconectado.
#
# CUÁNDO USARLO:
#   - Ejercicios tipo "Necessary Cities":
#       "una ciudad es necesaria si al borrarla, algunas otras
#        dejan de estar conectadas entre sí".
#
# CÓMO USARLO:
#   1) Construir el grafo NO DIRIGIDO:
#         graph = [[] for _ in range(n)]
#         graph[u].append(v)
#         graph[v].append(u)
#   2) Llamar:
#         articulation_points = find_articulation_points(graph)
#   3) articulation_points = lista de nodos (0-based) que son
#      puntos de articulación.
# ============================================================

def find_articulation_points(graph):
    node_count = len(graph)
    visited = [False] * node_count
    discovery_time = [0] * node_count
    low = [0] * node_count
    is_articulation = [False] * node_count
    time_counter = [0]

    def dfs_articulation(current, parent):
        visited[current] = True
        time_counter[0] += 1
        discovery_time[current] = low[current] = time_counter[0]
        child_count = 0  # hijos en el árbol de DFS

        for neighbor in graph[current]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                # back-edge
                low[current] = min(low[current], discovery_time[neighbor])
            else:
                dfs_articulation(neighbor, current)
                low[current] = min(low[current], low[neighbor])
                child_count += 1

                # Caso general: si low[neighbor] >= discovery_time[current],
                # entonces current es punto de articulación
                if parent != -1 and low[neighbor] >= discovery_time[current]:
                    is_articulation[current] = True

        # Caso especial: la raíz del DFS es punto de articulación
        # solo si tiene más de un hijo en el árbol DFS
        if parent == -1 and child_count > 1:
            is_articulation[current] = True

    for start_node in range(node_count):
        if not visited[start_node]:
            dfs_articulation(start_node, -1)

    articulation_points = [node for node, flag in enumerate(is_articulation) if flag]
    return articulation_points
