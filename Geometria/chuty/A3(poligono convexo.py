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
    
def orient(a: Punto, b: Punto, c: Punto) -> float:
    """
    Orientación del triplete (a, b, c):
        > 0  → giro antihorario (izquierda)
        < 0  → giro horario (derecha)
        = 0  → colineales. (se tocan)
    Implementa: (b - a) × (c - a)
    """
    return (b - a) ^ (c - a)
    
N = int(input())
puntos = []
    
for _ in range(N):
    x,y = map(int, input().split())
    puntos.append(Punto(x,y))
    
orientacion = 0 
convexo = True
    
for i in range(N):
    a = puntos[i]
    b = puntos[(i+1) % N]
    c = puntos[(i+2) % N]
    
    value = orient(a,b,c)
    if value == 0: # Puntos colineales no cambian curvatura
        continue
    
    if orientacion == 0: # El primer giro, define la curvatura
        orientacion = value
        continue
    
    if (orientacion > 0 and value < 0) or (orientacion < 0 and value > 0):
        convexo=False
        break
    
print("YES" if convexo else "NO")

