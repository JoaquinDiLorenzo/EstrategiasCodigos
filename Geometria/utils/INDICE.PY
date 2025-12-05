###############################################
# ÍNDICE RÁPIDO – GEOMETRÍA (QUÉ USAR SEGÚN LA CONSIGNA)
###############################################
# Idea: leo la consigna, busco una frase parecida a estas,
# y de ahí sé QUÉ hacer y DÓNDE buscar la plantilla / util.

# ─────────────────────────────────────────────
# 1) POSICIÓN RELATIVA DE UN PUNTO RESPECTO A UNA LÍNEA
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Determinar si el punto C está a la izquierda, derecha o sobre la línea AB"
#   - "Point location test"
#   - "¿En qué lado de la recta queda el punto?"
#
# Usar:
#   Archivo: VECTORES.py
#   Función: orient(a, b, c)
#            >0  → LEFT
#            <0  → RIGHT
#            =0  → TOUCH / ON LINE
#
# Plantilla:
#   from utils.PUNTO import Punto
#   from utils.VECTORES import orient, EPS
#
#   o = orient(a, b, c)
#   if abs(o) <= EPS: print("TOUCH")
#   elif o > 0:       print("LEFT")
#   else:             print("RIGHT")


# ─────────────────────────────────────────────
# 2) ¿POLÍGONO CONVEXO? (CONVEX POLYGON)
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Chequear si un polígono es convexo"
#   - "Todos los ángulos apuntan para el mismo lado"
#
# Usar:
#   Archivo: VECTORES.py
#   Función: orient(a, b, c)
#
# Idea:
#   - Recorrer triples consecutivos (pi, pi+1, pi+2)
#   - Mirar el signo de orient en cada uno
#   - Si cambia de signo → NO convexo
#
# Plantilla:
#   for i in range(n):
#       a, b, c = pts[i], pts[(i+1)%n], pts[(i+2)%n]
#       o = orient(a, b, c)
#   → decidir por los signos.


# ─────────────────────────────────────────────
# 3) DISTANCIAS / PAREJA MÁS CERCANA DE PUNTOS
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Encontrar la distancia mínima entre dos puntos"
#   - "Closest pair / closest points"
#
# Usar:
#   Archivo: VECTORES.py
#   Función: dist2(a, b)  (mejor que dist para comparar)
#
# Plantilla:
#   best = INF
#   for i in range(n):
#       for j in range(i+1, n):
#           best = min(best, dist2(pts[i], pts[j]))
#   print(best**0.5)


# ─────────────────────────────────────────────
# 4) RELACIÓN ENTRE DOS RECTAS INFINITAS (LINES)
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Dadas dos rectas, indicar si son paralelas, la misma o se cruzan"
#   - "Lines / line classification"
#   - "Trabajamos con rectas infinitas, no tramos"
#
# Usar:
#   Archivo: LINEA.py
#   Función: line_relation(p1, p2, p3, p4)
#
# Devuelve:
#   ("SAME", None)
#   ("PARALLEL", None)
#   ("INTERSECT", Punto)
#
# Plantilla:
#   tipo, P = line_relation(p1, p2, p3, p4)
#   if tipo == "SAME":     print("SAME")
#   elif tipo == "PARALLEL": print("PARALLEL")
#   else:                 print(P.x, P.y)


# ─────────────────────────────────────────────
# 5) INTERSECCIÓN DE SEGMENTOS (TRAMOS FINITOS)
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Determinar si dos segmentos se cruzan"
#   - "Segment intersection"
#   - "Hay colisión entre estos dos tramos?"
#
# Usar:
#   Archivo: INTERSECCION.py
#   Función: segments_intersect(p1, p2, p3, p4) → bool
#
# Plantilla:
#   from utils.INTERSECCION import segments_intersect
#   if segments_intersect(p1, p2, p3, p4): print("YES")
#   else:                                 print("NO")


# ─────────────────────────────────────────────
# 6) ÁREA DE POLÍGONO (SHOELACE)
# ─────────────────────────────────────────────
# Frases típicas:
#   - "Calcular el área de un polígono"
#   - "Imprimir 2 * área del polígono"
#   - "Polygon area"
#
# Usar:
#   Archivo: PUNTO.py
#   Operador: p ^ q  (producto cruzado)
#
# Fórmula:
#   area2 = sum( pts[i] ^ pts[(i+1)%n] )
#   área = abs(area2) / 2
#
# Plantilla:
#   area2 = 0
#   for i in range(n):
#       area2 += pts[i] ^ pts[(i+1)%n]
#   print(abs(area2))     # si piden 2*area
#   # o print(abs(area2)/2) si piden el área normal


# ─────────────────────────────────────────────
# 7) CHEQUEAR SI UN PUNTO ESTÁ SOBRE UNA RECTA
# ─────────────────────────────────────────────
# Frases típicas:
#   - "¿El punto P pertenece a la recta AB?"
#   - "Point on line / colinealidad pura"
#
# Usar:
#   Archivo: VECTORES.py  (orient)
#   o helper point_on_line(a, b, p) si lo tenés definido
#
# Plantilla (simple con orient):
#   if abs(orient(a, b, p)) <= EPS:   # colineales
#       print("ON LINE")
#   else:
#       print("NO")


# ─────────────────────────────────────────────
# 8) RESUMEN EXPRESS (QUÉ PENSAR PRIMERO)
# ─────────────────────────────────────────────
# 1) ¿Hablan de izquierda/derecha, sentido del giro, convexidad?
#       → usar orient(a, b, c) (VECTORES.py)
#
# 2) ¿Hablan de segmentos que se cortan o colisionan?
#       → usar segments_intersect (INTERSECCION.py)
#
# 3) ¿Hablan de rectas infinitas (no segmentos)?
#       → usar line_relation (LINEA.py)
#
# 4) ¿Hablan de distancia mínima / par más cercano?
#       → usar dist2(a, b) (VECTORES.py) y quedarme con el mínimo.
#
# 5) ¿Hablan de área de un polígono?
#       → usar suma de cross products pts[i] ^ pts[i+1] (PUNTO.py).
#
# 6) ¿Solo preguntan si un punto está en la recta?
#       → orient(a, b, p) == 0  (o |orient| <= EPS).
###############################################