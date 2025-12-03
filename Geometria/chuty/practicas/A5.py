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

# se pide determinar si los segmentos de la linea dados se intersecan (tienen un punto en comun), por lo que se necesita:
# construir el vector entre dos puntos (resta)
# y chequear la orientacion (xor)
def orient(a: Punto, b: Punto, c: Punto):
    # devuelve el signo de a -> b -> c
    cross = (b - a) ^ (c - a)
    if cross > 0:
        return 1
    if cross < 0:
        return -1
    return 0

def on_segment(a: Punto, b: Punto, c: Punto):
    # devuelve si c esta en el segmento [a, b]
    return (min(a.x, b.x) <= c.x <= max(a.x, b.x) and
            min(a.y, b.y) <= c.y <= max(a.y, b.y))

def intersect(p1: Punto, p2: Punto, p3: Punto, p4: Punto):
    # chequea si los segmentos [p1,p2] y [p3,p4] se intersecan
    o1 = orient(p1, p2, p3)
    o2 = orient(p1, p2, p4)
    o3 = orient(p3, p4, p1)
    o4 = orient(p3, p4, p2)

    # se cruzan en cruz:
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    # sasos especiales: colineales y apoyados en el segmento
    if o1 == 0 and on_segment(p1, p2, p3):
        return True
    if o2 == 0 and on_segment(p1, p2, p4):
        return True
    if o3 == 0 and on_segment(p3, p4, p1):
        return True
    if o4 == 0 and on_segment(p3, p4, p2):
        return True

    return False

t = int(sys.stdin.readline())

tests = []

for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    tests.append((Punto(x1, y1), Punto(x2, y2), Punto(x3, y3), Punto(x4, y4)))

for p1, p2, p3, p4 in tests:
    sys.stdout.write("YES\n" if intersect(p1, p2, p3, p4) else "NO\n")