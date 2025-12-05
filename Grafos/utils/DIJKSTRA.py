# ============================================================
# DIJKSTRA (camino mínimo con pesos positivos)
#
# PARA QUÉ SIRVE:
#   - Encontrar la DISTANCIA MÍNIMA desde un nodo origen
#     hacia TODOS los demás, en un grafo dirigido o no dirigido
#     con PESOS NO NEGATIVOS.
#
# CÓMO CONSTRUIR EL GRAFO:
#   graph = [[] for _ in range(n)]
#   for _ in range(m):
#       a, b, c = map(int, input().split())
#       a -= 1   # pasar a 0-based
#       b -= 1
#       graph[a].append((b, c))   # si es dirigido
#       graph[b].append((a, c))   # agregar también si es NO DIRIGIDO
#
# CÓMO USAR DIJKSTRA:
#   distances = dijkstra(0, graph, n)   # 0 = ciudad 1
#   luego imprimir distances[i] para i=0..n-1
# ============================================================

import heapq
INF = 10**18

def dijkstra(start_node, graph, node_count):
    distances = [INF] * node_count
    distances[start_node] = 0
    heap = [(0, start_node)]   # (distancia actual, nodo)

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current_dist > distances[current]:
            continue   # ya tenemos una distancia mejor

        for neighbor, weight in graph[current]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances