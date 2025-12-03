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
    
    def mod(self) -> float: # distancia entre dos puntos
        return (self.x**2 + self.y**2)**0.5

n = int(sys.stdin.readline())

points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append(Punto(x, y))

best = float('inf') # se inicializa el mejor en infinito

# se pide la menor distancia entre puntos, por lo que:
# se necesita restar los dos puntos para obtener el vector entre dos puntos (resta)
# y se necesita computar la distancia (mod())
for i in range(n):
    for j in range(i+1, n):
        d = (points[i] - points[j]).mod()
        if d < best:
            best = d

sys.stdout.write(f"{best:.10f}")