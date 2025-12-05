# ============================================================
# FUNCIONES BÁSICAS DE GEOMETRÍA VECTORIAL
#
# PARA QUÉ SIRVE:
#   - Medir distancias entre puntos.
#   - Calcular orientación (giro horario / antihorario),
#     que es esencial para:
#       * intersección de segmentos
#       * envolvente convexa
#       * clasificación de puntos
#
# CÓMO USAR:
#   from geom import Punto, dist, orient
#
#   a = Punto(0, 0)
#   b = Punto(3, 4)
#
#   print(dist(a, b))     # 5.0
#   print(orient(a, b, Punto(1, 1)))  # >0 = antihorario
#
# EJEMPLO RÁPIDO:
#   a = Punto(0, 0)
#   b = Punto(4, 0)
#   c = Punto(2, 3)
#   print(orient(a, b, c))  # >0 => forma giro antihorario
# -------
# dist2(a, b):
#   - Calcula la distancia **al cuadrado**.
#   - NO usa raíz cuadrada → es más rápido y exacto.
#   - Ideal para:
#       * comparar distancias
#       * encontrar mínimos
#       * evitar errores de floating point
#   - Usar SIEMPRE durante el cálculo.
#
# dist(a, b):
#   - Calcula la distancia real (euclidiana).
#   - Usa sqrt → más lento y con error numérico.
#   - Usar SOLO cuando el problema pide:
#       * imprimir la distancia real
#       * precisión con error permitido (ej: 1e-6)
#
# Regla general:
#   - Computar todo con dist2.
#   - Al final, si la salida lo exige, imprimir sqrt(dist2_min).
# ============================================================

from .punto import Punto, EPS

def dist2(a: Punto, b: Punto) -> float:
    """Distancia al cuadrado (evita la raíz)."""
    return (a.x - b.x)**2 + (a.y - b.y)**2

def dist(a: Punto, b: Punto) -> float:
    """Distancia euclidiana."""
    return dist2(a, b)**0.5

def orient(a: Punto, b: Punto, c: Punto) -> float:
    """
    Orientación del triplete (a, b, c):
        > 0  → giro antihorario (izquierda)
        < 0  → giro horario (derecha)
        = 0  → colineales. (se tocan)
    Implementa: (b - a) × (c - a)
    """
    return (b - a) ^ (c - a)
