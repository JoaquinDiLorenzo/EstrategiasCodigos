import sys

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    
    def __mul__(self, escalar: float):
        return Punto(self.x * escalar, self.y * escalar)
    
    def __dot__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __xor__(self, other):
        return self.x * other.y - self.y * other.x
    
    def mod(self) -> float:
        return (self.x**2 + self.y**2)**0.5

n = int(sys.stdin.readline())

vertex = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    vertex.append(Punto(x, y))

# se pide el area de un poligono, por lo que se usa la formula del shoelace (xor)
# o sea, la sumatoria del producto cruzado entre los puntos tomados como vectores desde el origen

area2 = 0  # 2 * area

for i in range(n):
    j = (i + 1) % n
    area2 += vertex[i] ^ vertex[j]

# se pide 2 * area (sin signo)
sys.stdout.write(f"{abs(area2)}")