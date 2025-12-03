import sys
sys.setrecursionlimit(10**7)

def dfs(v, parent, graph, visited, order):
    """
    Realiza una búsqueda en profundidad (DFS) desde el nodo `v`,
    visitando recursivamente todos los nodos alcanzables.

    Este DFS es genérico y sirve como base para:
        * Encontrar componentes conexas.
        * Generar un árbol DFS.
        * Detectar ciclos en grafos no dirigidos.
        * Guardar el orden de recorrido.
        * Preparar algoritmos avanzados (articulación, puentes, SCC si se adapta).

    Parámetros:
        v (int):
            Nodo actual desde el cual se realiza la exploración.
            Debe estar indexado dentro de 0..n-1.

        parent (int):
            Padre del nodo `v` dentro del árbol DFS.
            Para el nodo raíz suele ser -1. Útil para evitar volver por la misma arista.

        graph (List[List[int]]):
            Lista de adyacencia. graph[u] contiene todos los vecinos del nodo u.

        visited (List[bool]):
            Arreglo booleano que marca qué nodos ya fueron visitados por la DFS.
            visited[u] == True significa que u ya se procesó o está en procesamiento.

        order (List[int]):
            Lista donde se almacena el orden en el que se visitan los nodos.
            Esto es útil para:
                - Depurar el recorrido.
                - Construir árboles DFS.
                - Generar órdenes postorder o preorder si se adapta.

    Proceso:
        1. Marca el nodo actual como visitado.
        2. Registra el nodo en `order` (preorder).
        3. Recorre todos los vecinos:
            - Si un vecino no fue visitado, llama DFS sobre él.
            - Si ya fue visitado y no es el padre, se detecta una arista de retroceso
              (lo cual indica un ciclo en grafos no dirigidos).

    Retorno:
        No retorna nada; modifica `visited` y `order` in-place.

    Complejidad:
        O(n + m), donde n es el número de nodos y m el número de aristas.

    Ejemplo de uso:
        visited = [False]*n
        order   = []
        dfs(0, -1, graph, visited, order)
        print("Recorrido:", order)
    """

    visited[v] = True
    order.append(v)

    for to in graph[v]:
        if to == parent:
            continue    # evita volver por la misma arista al padre

        if not visited[to]:
            dfs(to, v, graph, visited, order)
        else:
            # Arista hacia un nodo ya visitado (back edge o cross edge)
            # Útil para detección de ciclos, análisis de estructura, etc.
            pass
