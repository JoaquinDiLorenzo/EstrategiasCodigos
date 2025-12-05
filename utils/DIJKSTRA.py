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
#       graph[a].append((b, c))   # vuelo dirigido a -> b con peso c
#       graph[b].append((a, c))   # En caso de ser NO DIRIGIDO
#
# CÓMO USAR DIJKSTRA:
#   dist = dijkstra(0, graph, n)   # 0 = ciudad 1
#   luego imprimir dist[i] para i=0..n-1
#                  print(*dist)
# ============================================================

import heapq
INF = 10**18

def dijkstra(start, graph, n):
    dist = [INF] * n
    dist[start] = 0
    heap = [(0, start)]   # (distancia actual, nodo)

    while heap:
        d, v = heapq.heappop(heap)

        if d > dist[v]:
            continue   # ya tenemos una distancia mejor

        for to, w in graph[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(heap, (nd, to))

    return dist
