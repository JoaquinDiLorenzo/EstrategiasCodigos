# ============================================================
# PUNTO 2D + OPERACIONES BÁSICAS
#
# PARA QUÉ SIRVE:
#   - Representar puntos y vectores en el plano.
#   - Hacer SUMA, RESTA, ESCALADO, NORMA y PRODUCTO CRUZADO.
#   - Es la base para TODOS los problemas de geometría:
#       * distancias
#       * orientación
#       * intersección de segmentos
#       * convexidad / envolvente convexa
#
# CÓMO USAR:
#   from geom.punto import Punto
#
#   p = Punto(2, 3)
#   q = Punto(-1, 4)
#
#   r = p + q          # suma de vectores
#   s = p - q          # resta de vectores
#   t = p * 2          # escala
#   area2 = (p ^ q)    # producto cruzado
#   d = p.norm()       # |p|
#
# EJEMPLO RÁPIDO:
#   p = Punto(0, 0)
#   q = Punto(3, 4)
#   print(q.norm())   # 5.0
# ============================================================

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
