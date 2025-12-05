# ============================================================
# PUENTES (Necessary Roads)
#
# PARA QUÉ SIRVE:
#   - Encontrar TODAS las aristas que, si las removés,
#     hacen que el grafo quede desconectado.
#
# CUÁNDO USARLO:
#   - Ejercicios tipo "Necessary Roads":
#       "una ruta es necesaria si al borrarla, algunas ciudades
#        dejan de estar conectadas entre sí".
#
# CÓMO USARLO:
#   1) Construir el grafo NO DIRIGIDO:
#         graph = [[] for _ in range(n)]
#         graph[u].append(v)
#         graph[v].append(u)
#   2) Llamar:
#         bridges = find_bridges(graph)
#   3) bridges = lista de pares (u, v) que son puentes (0-based).
# ============================================================

def find_bridges(graph):
    node_count = len(graph)
    visited = [False] * node_count
    discovery_time = [0] * node_count
    low = [0] * node_count
    bridges = []
    time_counter = [0]  # usamos lista para poder modificar dentro del dfs

    def dfs_bridges(current, parent):
        visited[current] = True
        time_counter[0] += 1
        discovery_time[current] = low[current] = time_counter[0]

        for neighbor in graph[current]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                # back-edge: actualizamos low con el tiempo de descubrimiento del vecino
                low[current] = min(low[current], discovery_time[neighbor])
            else:
                dfs_bridges(neighbor, current)
                low[current] = min(low[current], low[neighbor])
                # Si low[neighbor] > discovery_time[current], (current, neighbor) es puente
                if low[neighbor] > discovery_time[current]:
                    bridges.append((current, neighbor))

    for start_node in range(node_count):
        if not visited[start_node]:
            dfs_bridges(start_node, -1)

    return bridges