# ============================================================
# INTERSECCIÓN DE SEGMENTOS EN 2D
#
# PARA QUÉ SIRVE:
#   - Saber si dos segmentos [p1,p2] y [p3,p4] se cruzan.
#   - Fundamental en:
#       * problemas de barreras
#       * caminos con obstáculos
#       * geometría analítica aplicada
#       * detectar colisiones
#
# ALGORITMO BASADO EN:
#   - ORIENTACIÓN de triples
#   - Caso general + casos colineales
#   - Función ON-SEGMENT del apunte
#
# CÓMO USAR:
#   from geom import Punto, segments_intersect
#
#   p1 = Punto(0, 0)
#   p2 = Punto(5, 5)
#   p3 = Punto(0, 5)
#   p4 = Punto(5, 0)
#
#   print(segments_intersect(p1, p2, p3, p4))  # True
#
# EJEMPLO RÁPIDO:
#   Segmentos cruzados:
#       (0,0)-(4,4) y (0,4)-(4,0)  → True
#   Segmentos paralelos sin tocarse:
#       (0,0)-(3,0) y (0,1)-(3,1)  → False
# ============================================================

from .punto import Punto, EPS
from .vectores import orient

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
