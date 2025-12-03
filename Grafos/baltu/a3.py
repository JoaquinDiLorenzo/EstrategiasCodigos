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

# se pide ir construyendo nuevas rutas, por lo que se usa el DSU
# tambien se pide el minimo de rutas requeridas
graph = DSU(n)

for _ in range(m):
    # se arma el grafo
    a, b = map(int, sys.stdin.readline().split())
    graph.union(a-1, b-1) # 1-indexado

# se busca un representante por componente conexa
representantes = []
for ciudad in range(n):
    if graph.getLink(ciudad) == ciudad:
        representantes.append(ciudad)

# si hay C componentes, se necesitan C-1 caminos
k = len(representantes)-1
sys.stdout.write(f"{k}\n")

# se conectan todas las componentes al priemr representante
for i in range(1, len(representantes)):
    sys.stdout.write(f"{representantes[0]+1} {representantes[i]+1}\n")