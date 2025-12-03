import math
    
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
    
    
def dist2(a: Punto, b: Punto) -> float:
    """Distancia al cuadrado (evita la raíz)."""
    return (a.x - b.x)**2 + (a.y - b.y)**2
    
def dist(a: Punto, b: Punto) -> float:
    """Distancia euclidiana."""
    return dist2(a, b)**0.5
    
def orient(a: Punto, b: Punto, c: Punto) -> float:
    """
    Orientación del triplete (a, b, c):
        > 0  → giro antihorario
        < 0  → giro horario
        = 0  → colineales.
    Implementa: (b - a) × (c - a)
    """
    return (b - a) ^ (c - a)
    
    
def closest_points(puntos):
    n = len(puntos)
    min_d2 = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            d2 = dist2(puntos[i], puntos[j])
            if d2 < min_d2:
                min_d2 = d2
    
    return math.sqrt(min_d2)
    
    
N = int(input())
puntos = []
    
for _ in range(N):
    x, y = map(float, input().split())
    puntos.append(Punto(x, y))
    
ans = closest_points(puntos)
print(f"{ans:.10f}")

