import heapq

INF = 10**18

def dijkstra(start, graph, n):
    """
    Implementación general del algoritmo de Dijkstra para calcular
    distancias mínimas desde un nodo origen `start` hacia todos los
    demás nodos de un grafo dirigido o no dirigido con pesos NO negativos.

    Este algoritmo es la herramienta estándar cuando:
        * Las aristas tienen peso >= 0.
        * Queremos caminos mínimos de un solo origen.
        * Necesitamos eficiencia O((n + m) log n), gracias al uso de un heap.

    Parámetros:
        start (int):
            Nodo desde el cual se calculan las distancias mínimas.
            Debe estar entre 0 y n-1.

        graph (List[List[Tuple[int, int]]]):
            Lista de adyacencia del grafo.
            Cada entrada graph[u] contiene tuplas (v, w):
                - v: vecino de u
                - w: peso de la arista u -> v

            Ejemplo:
                graph[u] = [(v1, w1), (v2, w2), ...]

        n (int):
            Cantidad total de nodos.

    Internamente:
        dist[v]: distancia mínima conocida desde `start` hasta `v`.
        heap   : cola de prioridad (min-heap) que almacena pares (distancia, nodo).
                  Garantiza que siempre se procese el nodo con menor distancia
                  actual conocida.

    Retorna:
        dist (List[int]):
            Arreglo donde dist[v] es la distancia mínima desde start hasta v.
            Si v es inalcanzable, dist[v] quedará en INF.

    Complejidad:
        O((n + m) log n), ideal para grafos grandes (hasta 2·10^5 aristas o más).

    Notas importantes:
        * Dijkstra solo funciona correctamente cuando los pesos w >= 0.
        * Si hay pesos negativos, se debe usar Bellman-Ford o SPFA.

    Ejemplo típico de uso:
        dist = dijkstra(0, graph, n)
        print(dist[destino])
    """

    dist = [INF] * n
    dist[start] = 0

    heap = [(0, start)]   # (distancia actual, nodo)

    while heap:
        d, v = heapq.heappop(heap)

        # Si el valor extraído no es óptimo, lo descartamos
        if d > dist[v]:
            continue

        # Relajación de aristas
        for to, w in graph[v]:
            nd = d + w   # nueva distancia tentativa
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(heap, (nd, to))

    return dist
