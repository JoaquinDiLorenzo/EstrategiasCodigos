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
        
def on_segment(a: Punto, b: Punto, p: Punto) -> bool:
    """
    p está en el rectángulo delimitado por a y b.
    Se usa SOLO cuando ya sabemos que son colineales.
    """
    return (min(a.x, b.x) - EPS <= p.x <= max(a.x, b.x) + EPS and
            min(a.y, b.y) - EPS <= p.y <= max(a.y, b.y) + EPS)
    
def segments_intersect(p1: Punto, p2: Punto, p3: Punto, p4: Punto) -> bool:
    """
    Determina si los segmentos [p1,p2] y [p3,p4] se intersectan.
    
    CASO GENERAL:
        orient(p3, p4, p1) y orient(p3, p4, p2) tienen signos opuestos
        Y
        orient(p1, p2, p3) y orient(p1, p2, p4) tienen signos opuestos
    
    CASOS COLINEALES:
        - p1 sobre [p3,p4]
        - p2 sobre [p3,p4]
        - p3 sobre [p1,p2]
        - p4 sobre [p1,p2]
    """
    d1 = orient(p3, p4, p1)
    d2 = orient(p3, p4, p2)
    d3 = orient(p1, p2, p3)
    d4 = orient(p1, p2, p4)
    
    # Caso general: signos opuestos
    if ((d1 > EPS and d2 < -EPS) or (d1 < -EPS and d2 > EPS)) and \
        ((d3 > EPS and d4 < -EPS) or (d3 < -EPS and d4 > EPS)):
        return True
    
    # Casos colineales
    if abs(d1) <= EPS and on_segment(p3, p4, p1):
        return True
    if abs(d2) <= EPS and on_segment(p3, p4, p2):
        return True
    if abs(d3) <= EPS and on_segment(p1, p2, p3):
        return True
    if abs(d4) <= EPS and on_segment(p1, p2, p4):
        return True
    
    return False
    
t = int(input())
    
for _ in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
    
    if segments_intersect(Punto(x1,y1), Punto(x2,y2), Punto(x3,y3), Punto(x4,y4)):
        print("YES")
    else:
        print("NO")