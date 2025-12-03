import sys, heapq

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


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c)) # 1-indexado con el peso agregado

# se pide determinar la longitud de la ruta mas corta entre 2 ciudades
# se va a usar un dijkstra (porque es un grafo pesado)
dist = dijkstra(0, graph, n)

for d in dist:
    sys.stdout.write(f"{d} ")