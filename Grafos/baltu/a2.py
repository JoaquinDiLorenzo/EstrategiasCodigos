import sys

class DSU:
    def __init__(self, n):
        self.link = [0] * n # Padre de cada nodo
        self.sz = [1] * n # Tamaño de cada componente
        for i in range(n):
            self.link[i] = i # Cada nodo es su propio padre
            
    def getLink(self, x):
        if self.link[x] != x: # Si no es su propio padre
            self.link[x] = self.getLink(self.link[x]) # Path compression
        return self.link[x]
            
    def union(self, x, y):
        x = self.getLink(x)
        y = self.getLink(y)
        if x != y: # Si no estan en la misma componente
            if self.sz[x] < self.sz[y]:
                x,y = y,x # Asegurarse de que x es la componente mas grande
            self.link[y] = x
            self.sz[x] += self.sz[y]
        return self.sz[x]

n, m = map(int, sys.stdin.readline().split())

# se pide inicializar el grafo sin rutas, e irlas agregando de a poco
# se tiene que usar el DSU para ir haciendo joins
graph = DSU(n)

components = n # numero de componentes conexas (al principio N)
size = 1 # tamaño inicial (al prinicpio 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if graph.getLink(a-1) != graph.getLink(b-1): # se construye una ruta entre nodos desconectados (1-indexado)
        components -= 1 # se reduce el num de componentes porque ahora son conexos

    size = max(size, graph.union(a-1, b-1)) # actualizo el size
    sys.stdout.write(f"{components} {size}\n") # cantidad de componentes y tamaño max de ese dia