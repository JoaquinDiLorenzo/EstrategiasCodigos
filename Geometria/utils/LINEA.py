# ============================================================
# LÍNEAS INFINITAS EN 2D (CLASIFICACIÓN + INTERSECCIÓN)
#
# PARA QUÉ SIRVE:
#   - Dadas dos rectas definidas por:
#         L1: p1 -- p2
#         L2: p3 -- p4
#     determina si:
#       * son la MISMA recta      → "SAME"
#       * son PARALELAS distintas → "PARALLEL"
#       * se INTERSECTAN en 1 pto → ("INTERSECT", Punto)
#
#   - Útil para problemas donde las rectas son INFINITAS,
#     no segmentos (a diferencia de INTERSECCION.py).
#
# CÓMO USAR (ejemplo típico del problema "Lines"):
#   p1 = Punto(x1, y1)
#   p2 = Punto(x2, y2)
#   p3 = Punto(x3, y3)
#   p4 = Punto(x4, y4)
#
#   tipo, P = line_relation(p1, p2, p3, p4)
#
#   if tipo == "SAME":
#       print("SAME")
#   elif tipo == "PARALLEL":
#       print("PARALLEL")
#   else:
#       print(f"{P.x:.10f} {P.y:.10f}")
#
# ============================================================

from utils.PUNTO import Punto, EPS
from utils.VECTORES import orient

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

# ============================================================
# CHEQUEAR SI UN PUNTO ESTÁ SOBRE UNA RECTA
# ============================================================

def point_on_line(p: Punto, a: Punto, b: Punto) -> bool:
    """
    Devuelve True si el punto p está sobre la RECTA infinita
    definida por a y b.

    Usa la orientación:
        orient(a, b, p) = 0  → colineales
    """
    return abs(orient(a, b, p)) <= EPS
