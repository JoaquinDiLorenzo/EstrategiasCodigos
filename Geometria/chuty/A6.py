EPS = 1e-9
    
class Punto:
    __slots__ = ("x", "y")
    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k: float):
        return Punto(self.x * k, self.y * k)
    
    __rmul__ = __mul__
    
    def __xor__(self, other):
        # PRODUCTO CRUZADO: det |x1 y1; x2 y2|
        return self.x * other.y - self.y * other.x
    
    def norm2(self):
        return self.x * self.x + self.y * self.y
    
    def norm(self):
        return self.norm2() ** 0.5
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
    
# Este es un porbelma clasico de producto cruzado
n = int(input())
puntos = []
area2 = 0
    
for _ in range(n):
    a,b = map(int, input().split())
    puntos.append(Punto(a,b))
    
for i in range(n):
    a = puntos[i]
    b = puntos[(i+1)%n]
    area2 += (a ^ b) #Usa la funcion de _XOR_ de la clase Punto
    
print(abs(area2))