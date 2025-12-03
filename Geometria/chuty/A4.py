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
        
def orient(a: Punto, b: Punto, c: Punto) -> float:
    """
    Orientación del triplete (a, b, c):
        > 0  → giro antihorario (izquierda)
        < 0  → giro horario (derecha)
        = 0  → colineales. (se tocan)
    Implementa: (b - a) × (c - a)
    """
    return (b - a) ^ (c - a)
    
def line_relation(p1: Punto, p2: Punto, p3: Punto, p4: Punto):
    """
    Clasifica dos rectas infinitas definidas por (p1,p2) y (p3,p4).
    
    Devuelve:
        ("SAME", None)              si son la misma recta
        ("PARALLEL", None)          si son paralelas distintas
        ("INTERSECT", Punto(x,y))   si se cortan en un único punto
    """
    # vectores dirección
    v = p2 - p1
    w = p4 - p3
    
    # producto cruzado v × w
    cross_vw = (v ^ w)
    
    # Caso 1: direcciones paralelas o colineales (cross_vw ~ 0)
    if abs(cross_vw) <= EPS:
        # Ver si son la misma recta:
        # Tomamos u = p3 - p1 y vemos si también es colineal con v
        u = p3 - p1
        if abs(u ^ v) <= EPS:
            return "SAME", None
        else:
            return "PARALLEL", None
    
    # Caso 2: se cruzan en un punto único
    # t = ((p3 - p1) × w) / (v × w)
    num = (p3 - p1) ^ w
    t = num / float(cross_vw)
    
    P = p1 + v * t
    return "INTERSECT", P
    
t = int(input())
    
for _ in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
    
    relation, intersection = line_relation(Punto(x1,y1), Punto(x2,y2), Punto(x3,y3), Punto(x4,y4))
    
    if intersection:
        print(f"{intersection.x:.10f} {intersection.y:.10f}")
    else:
        print(relation)

