from collections import deque

def bfs(start, end, graph, n):
    """
    Realiza una búsqueda en anchura (BFS) desde un nodo origen `start`
    en un grafo no ponderado, obteniendo:

        - Las distancias mínimas desde `start` a todos los nodos alcanzables.
        - El camino más corto desde `start` hasta `end`, si existe.

    Este BFS es general y sirve para:
        * Encontrar caminos mínimos en grafos sin pesos.
        * Detectar conectividad.
        * Reconstruir rutas mediante el vector de padres.
        * Resolver problemas clásicos como "Message Route", "Shortest Path",
          o cualquier variante donde las aristas tengan peso 1.

    Parámetros:
        start (int): nodo desde el cual se inicia el recorrido.
                     Debe estar indexado entre 0 y n-1.
        end   (int): nodo destino cuyo camino queremos reconstruir.
                     También debe estar entre 0 y n-1.
        graph (List[List[int]]): lista de adyacencia del grafo.
                                 graph[v] contiene los vecinos del nodo v.
        n     (int): cantidad total de nodos del grafo.

    Internamente se mantienen dos estructuras clave:
        - dist[v]: distancia mínima desde start hasta v.
                   Toma valor -1 si v es inalcanzable.
        - parent[v]: nodo anterior en el camino mínimo hacia v.
                     Es -1 para el nodo start y para nodos no visitados.

    Retorna:
        Si `end` es alcanzable:
            (dist, path)
            donde:
                dist (List[int]): distancias mínimas desde start a cada nodo.
                path (List[int]): lista con el camino mínimo reconstruido,
                                   desde start hasta end inclusive.

        Si `end` NO es alcanzable:
            None

    Complejidad:
        O(n + m), donde m es la cantidad de aristas.
        BFS es óptimo para grafos no ponderados.

    Ejemplo de uso:
        dist, path = bfs(0, 7, graph, n)
        print("Distancia:", dist[7])
        print("Camino:", path)
    """

    dist = [-1] * n       # distancia mínima desde start
    parent = [-1] * n     # para reconstrucción del camino
    dist[start] = 0

    q = deque([start])

    while q:
        v = q.popleft()
        for to in graph[v]:
            if dist[to] == -1:             # no visitado todavía
                dist[to] = dist[v] + 1
                parent[to] = v
                q.append(to)

    # Si end no fue alcanzado, no existe camino
    if dist[end] == -1:
        return None

    # Reconstrucción del camino mínimo end → start usando parent[]
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist, path
