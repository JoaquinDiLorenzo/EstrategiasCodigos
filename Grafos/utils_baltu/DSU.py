# DSU SIN PATH COMPRESSION
# Complejidad: O(n) para n uniones en el peor caso
# Memoria: O(n)

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