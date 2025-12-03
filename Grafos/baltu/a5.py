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
            return True # ajuste para mostrar que se unen dos componentes distintas
        return False # ya estaban en el mismo conjunto
    
def kruskal(n, edges):
    edges.sort()          # ordenar por costo creciente
    graph = DSU(n)
    total_cost = 0
    used_edges = 0

    for cost, u, v in edges:
        if graph.union(u, v):           # une si estaban en componentes distintas
            total_cost += cost
            used_edges += 1

    return total_cost, used_edges

n, m = map(int, sys.stdin.readline().split())

# se pide computar el minimo costo de reparacion de rutas pesadas
# para eso se usa kruskal, que permite averiguar el arbol de expansion minima (costo minimo de conectar todos los nodos)
edges = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a-1, b-1)) # 1-indexado

costo_total, aristas_usadas = kruskal(n, edges)

if aristas_usadas != n-1:
    sys.stdout.write("IMPOSSIBLE")
else:
    sys.stdout.write(f"{costo_total}")