###############################################
# BINARY SEARCH – RESUMEN RÁPIDO DE PATRONES
###############################################
#
# 1) SOBRE ARREGLO ORDENADO (array):
#    - Buscar un valor exacto:      binary_search_exact(arr, x)
#    - Primer índice con arr[i] >= x:  lower_bound(arr, x)
#    - Primer índice con arr[i] >  x:  upper_bound(arr, x)
#
# 2) SOBRE RESPUESTA (rango [low, high]):
#    - Queremos el MÍNIMO x que cumple check(x):  binary_search_min(low, high, check)
#    - Queremos el MÁXIMO x que cumple check(x):  binary_search_max(low, high, check)
#
# Donde check(x) es una función MONÓTONA:
#   False False ... False True True ... True   (para min)
#   True  True  ... True  False False ... False (para max)
#
# Usos típicos en los ejercicios del parcial:
#   - Dividir en K segmentos minimizando el máximo (sumas, cargas) → BS sobre respuesta.
#   - Encontrar cuántos elementos cumplen cierta condición en un array ordenado → lower/upper_bound.
#   - Encontrar el primer/último índice donde algo se cumple → variantes de lo mismo.
###############################################

###############################################
# 1️⃣ BINARY SEARCH SOBRE RESPUESTA – MÍNIMO x TAL QUE check(x) ES True
###############################################

def binary_search_min(low, high, check):
    """
    Busca el valor mínimo en el rango entero [low, high] que cumple la condición 'check'.

    PRECONDICIÓN:
        - check(x) es MONÓTONA:
            False False ... False True True ... True
        - Es decir:
            si check(x) es True, entonces check(y) también es True para todo y > x.

    Args:
        low  (int): límite inferior del rango de búsqueda.
        high (int): límite superior del rango de búsqueda.
        check (function): función que recibe un entero x y devuelve True/False.

    Returns:
        int | None: el mínimo x en [low, high] tal que check(x) es True,
                    o None si NINGÚN x cumple la condición.
    """
    ans = None

    while low <= high:
        mid = (low + high) // 2

        if check(mid):
            ans = mid        # mid es válido, lo guardamos
            high = mid - 1   # buscamos algo más chico a la izquierda
        else:
            low = mid + 1    # necesitamos un valor más grande

    return ans


###############################################
# 2️⃣ BINARY SEARCH SOBRE RESPUESTA – MÁXIMO x TAL QUE check(x) ES True
###############################################

def binary_search_max(low, high, check):
    """
    Busca el valor máximo en el rango entero [low, high] que cumple la condición 'check'.

    PRECONDICIÓN:
        - check(x) es MONÓTONA:
            True True ... True False False ... False
        - Es decir:
            si check(x) es True, entonces check(y) también es True para todo y < x.

    Args:
        low  (int): límite inferior del rango de búsqueda.
        high (int): límite superior del rango de búsqueda.
        check (function): función que recibe un entero x y devuelve True/False.

    Returns:
        int | None: el máximo x en [low, high] tal que check(x) es True,
                    o None si NINGÚN x cumple la condición.
    """
    ans = None

    while low <= high:
        mid = (low + high) // 2

        if check(mid):
            ans = mid        # mid es válido, lo guardamos
            low = mid + 1    # buscamos algo más grande a la derecha
        else:
            high = mid - 1   # necesitamos un valor más chico

    return ans


###############################################
# 3️⃣ BINARY SEARCH EN ARREGLO ORDENADO – VALOR EXACTO
###############################################

def binary_search_exact(arr, x):
    """
    Devuelve un índice i tal que arr[i] == x, o -1 si no existe.
    Requiere que 'arr' esté ORDENADO.

    COMPLEJIDAD: O(log n)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


###############################################
# 4️⃣ LOWER_BOUND – PRIMER ÍNDICE CON arr[i] >= x
###############################################

def lower_bound(arr, x):
    """
    Devuelve el primer índice i tal que arr[i] >= x.
    Si TODOS los elementos son < x, devuelve len(arr).

    Es el equivalente a std::lower_bound de C++.

    ÚTIL PARA:
        - contar cuántos elementos son >= x (n - i)
        - encontrar dónde insertar x para mantener orden
    """
    low, high = 0, len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1   # busco algo más a la izquierda
        else:
            low = mid + 1

    return ans


###############################################
# 5️⃣ UPPER_BOUND – PRIMER ÍNDICE CON arr[i] > x
###############################################
# CÓMO CONTAR ELEMENTOS EN UN INTERVALO USANDO BINARY SEARCH
#
# Notación matemática: queremos contar elementos x tales que:
#   L ≤ x ≤ R   ó   L < x ≤ R   ó   L ≤ x < R   ó   L < x < R
#
# En un array ORDENADO arr, las funciones estándar:
#
#   lower_bound(v)  → primer índice i tal que arr[i] >= v
#   upper_bound(v)  → primer índice i tal que arr[i] >  v
#
# Para todos los casos, SIEMPRE se usa:
#   cantidad = indice_derecha - indice_izquierda
#
# No es "inverso": es la forma correcta de contar posiciones.
###############################################################

###############################################################
# 1) Intervalo CERRADO [L, R]
#    Queremos: L ≤ x ≤ R
#
#  izquierda = lower_bound(L)
#  derecha   = upper_bound(R)
#  cantidad  = derecha - izquierda
###############################################################

# Representación
#  [L, R]  →  lower_bound(L), upper_bound(R)

###############################################################
# 2) Intervalo (L, R]    (excluye L, incluye R)
#    Queremos: L < x ≤ R
#
#    Equivale a: x ≥ (L+1) si trabajamos con enteros
#
#  izquierda = lower_bound(L+1)
#  derecha   = upper_bound(R)
#  cantidad  = derecha - izquierda
###############################################################

# Representación
#  (L, R]  →  lower_bound(L+1), upper_bound(R)

###############################################################
# 3) Intervalo [L, R)    (incluye L, excluye R)
#    Queremos: L ≤ x < R
#
#  izquierda = lower_bound(L)
#  derecha   = lower_bound(R)
#  cantidad  = derecha - izquierda
###############################################################

# Representación
#  [L, R)  →  lower_bound(L), lower_bound(R)

###############################################################
# 4) Intervalo (L, R)    (excluye extremos)
#    Queremos: L < x < R
#
#  izquierda = upper_bound(L)
#  derecha   = lower_bound(R)
#  cantidad  = derecha - izquierda
###############################################################

# Representación
#  (L, R)  →  upper_bound(L), lower_bound(R)
###############################################################

def upper_bound(arr, x):
    """
    Devuelve el primer índice i tal que arr[i] > x.
    Si NINGÚN elemento es > x, devuelve len(arr).

    Es el equivalente a std::upper_bound de C++.

    ÚTIL PARA:
        - contar cuántas apariciones de x hay:
              cnt = upper_bound(arr, x) - lower_bound(arr, x)
        - contar cuántos son <= x
    """
    low, high = 0, len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1   # busco algo más a la izquierda
        else:
            low = mid + 1

    return ans


###############################################
# 6️⃣ NOTA SOBRE check() PARA BS SOBRE RESPUESTA
###############################################
# En muchos problemas (como cortar array en K partes, o “¿es posible con X?”),
# vas a definir una función check(mid, ...) aparte.
#
# Ejemplo típico (el que ya tenés en check.py):
#
# def es_posible(max_suma, k, array):
#     # ¿Se puede dividir 'array' en a lo sumo k segmentos contiguos
#     #  tal que la suma de cada uno <= max_suma?
#     suma = 0
#     cant_sub = 1
#
#     for x in array:
#         if x > max_suma:
#             return False  # ni siquiera un solo elemento entra
#         if suma + x > max_suma:
#             cant_sub += 1
#             suma = 0
#         suma += x
#
#     return cant_sub <= k
#
# Y en el main:
#
#   low  = max(array)       # mínimo posible
#   high = sum(array)       # máximo posible
#
#   def check(mid):
#       return es_posible(mid, k, array)
#
#   mejor = binary_search_min(low, high, check)
#   print(mejor)
#
###############################################
# FIN PLANTILLAS BINARY SEARCH
###############################################