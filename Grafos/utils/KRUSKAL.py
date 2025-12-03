class DSU:
    """
    Estructura Disjoint Set Union (Union-Find) con compresión de caminos
    y unión por tamaño. Permite mantener particiones dinámicas de un conjunto
    de vértices y consultar rápidamente si dos vértices pertenecen a la misma
    componente conexa.

    Este DSU está optimizado para usarse en el algoritmo de Kruskal:  
    - getLink(x) aplica path compression, logrando casi O(1) amortizado.  
    - union(x, y) aplica union-by-size para mantener árboles planos.

    Parámetros:
        n (int): cantidad de nodos (0 .. n-1)

    Atributos:
        link (List[int]): link[i] es el padre de i en el bosque de conjuntos.
                          Si link[i] == i, entonces i es representante (root).
        sz   (List[int]): tamaño del conjunto cuya raíz es cada nodo.
    """

    def __init__(self, n):
        self.link = [0] * n       # Padre de cada nodo
        self.sz = [1] * n         # Tamaño de cada conjunto
        for i in range(n):
            self.link[i] = i      # Cada nodo arranca como su propio padre

    def getLink(self, x):
        """
        Encuentra la raíz (representante) del conjunto al que pertenece x.
        Utiliza *path compression*, que aplana el árbol de padres y permite
        futuras búsquedas prácticamente O(1).

        Retorna:
            int: representante del conjunto de x.
        """
        if self.link[x] != x:
            self.link[x] = self.getLink(self.link[x])  # Path compression
        return self.link[x]

    def union(self, x, y):
        """
        Une los conjuntos que contienen a x y a y, si son distintos.
        Implementa *union by size*: la raíz con mayor tamaño absorbe a la otra,
        manteniendo árboles más bajos y eficientes.

        Parámetros:
            x (int), y (int): nodos a unir.

        Retorna:
            bool: True si se unieron dos componentes diferentes.
                  False si ya estaban en el mismo conjunto.
        """
        x = self.getLink(x)
        y = self.getLink(y)
        if x != y:
            if self.sz[x] < self.sz[y]:
                x, y = y, x        # Garantiza que x sea la raíz más grande
            self.link[y] = x       # y pasa a depender de x
            self.sz[x] += self.sz[y]
            return True
        return False



def kruskal(n, edges):
    """
    Implementación general del algoritmo de Kruskal para hallar un
    Árbol de Expansión Mínima (MST) en un grafo no dirigido ponderado.

    Requisitos:
        - El grafo puede estar desconectado; Kruskal encontrará un MST
          si el grafo es conexo, o un bosque generador mínimo si no lo es.
        - Las aristas deben venir como tuplas (costo, u, v),
          donde u y v son nodos 0-indexados.

    Parámetros:
        n (int): cantidad de nodos del grafo.
        edges (List[Tuple[int,int,int]]): lista de aristas en formato
                                          (costo, u, v).

    Proceso:
        1. Ordena todas las aristas por costo creciente.
        2. Inicializa un DSU con n conjuntos (uno por nodo).
        3. Recorre las aristas en orden creciente:
            - Si u y v están en distintas componentes, se agrega la arista
              al MST y se unen ambas componentes en el DSU.
        4. La suma de los costos seleccionados da el costo total del MST.

    Retorna:
        (total_cost, used_edges):
            total_cost (int): costo total del MST.
            used_edges (int): cantidad de aristas incorporadas al MST.
                              Para un grafo conexo debe ser n-1.
    """

    # Ordenación por costo creciente
    edges.sort()

    dsu = DSU(n)
    total_cost = 0
    used_edges = 0

    for cost, u, v in edges:
        # Si une componentes distintas, pertenece al MST
        if dsu.union(u, v):
            total_cost += cost
            used_edges += 1

    return total_cost, used_edges
