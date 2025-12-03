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

# se pide determinar si un poligono es convexo a partir de sus puntos,
# por lo que se necesita fijarse si de a tres vertices, estos van en la misma direccion
# se va a necesitar la operacion XOR

if n < 3: # menos de 3 puntos, no hay poligonos
    sys.stdout.write("NO")
    sys.exit(0)

signo = 0 # +1 a contrarreloj, -1 en sentido de las agujas

for i in range(n):
    a = vertex[i]
    b = vertex[(i+1) % n]
    c = vertex[(i+2) % n]

    v1 = b - a
    v2 = c - b
    cross = v1 ^ v2

    if cross == 0:
        # colineal, no define el giro
        continue
    
    actual = 1 if cross > 0 else -1

    if signo == 0:
        signo = actual
    elif actual != signo:
        sys.stdout.write("NO")
        sys.exit(0)

# si nunca hubo giro no nulo, son todos colineales, por lo que no es convexo
if signo == 0:
    sys.stdout.write("NO")
else:
    sys.stdout.write("YES")