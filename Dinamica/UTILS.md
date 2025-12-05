###############################################
# DP – IDENTIFICACIÓN RÁPIDA (RESUMEN MENTAL)
###############################################
# Mirá la consigna, buscá frases parecidas a estas y elegí la plantilla.

# 1. Orden importa → COUNT PERMUTATIONS → dp[x] += dp[x−move]
#       (dp_count_permutations)
#   Frases típicas:
#       - "¿De cuántas maneras se puede obtener la suma X?"
#       - "¿Cuántas formas de llegar a X usando estos movimientos/monedas?"
#       - "Todas las secuencias distintas cuentan como diferentes."
#       - "2+3+4 y 3+2+4 deben contarse por separado."
#
# 2. Minimizar → dp[x] = min(dp[x], dp[x−c] + costo)
#       (dp_min_cost)
#   Frases típicas:
#       - "Encontrar el mínimo número de ... para llegar a X."
#       - "Calcular el costo mínimo / número mínimo de pasos."
#       - "Minimizar el número de monedas / operaciones / movimientos."
#       - "¿Cuál es la cantidad mínima necesaria para...?"
#
# 3. Orden NO importa → COUNT COMBINATIONS → loop monedas afuera
#       (dp_combinations_no_order)
#   Frases típicas:
#       - "Calcular el número de combinaciones para obtener la suma X."
#       - "2+3 y 3+2 se consideran la misma combinación."
#       - "Subconjuntos de monedas / elementos que suman X."
#       - "Número de formas de elegir elementos (sin importar el orden)."
#
# 4. Booleano / subset → dp[x] = dp[x] or dp[x−val]
#       (dp_subset_sum)
#   Frases típicas:
#       - "Determinar si es posible obtener la suma X."
#       - "¿Existe algún subconjunto que cumpla ...?"
#       - "Responder SÍ/NO si se puede lograr tal suma / condición."
#       - "¿Se puede llenar exactamente capacidad X?"
#
# 5. Dos secuencias → LCS → dp[i][j]
#       (dp_lcs_length)
#   Frases típicas:
#       - "Longitud de la subsecuencia común más larga."
#       - "Subsecuencia común más larga entre dos cadenas/secuencias."
#       - "Medir similitud entre dos strings mediante subsecuencias."
#       - "Encontrar cuántos elementos en común se pueden alinear manteniendo el orden."
#
# 6. Peso/valor → Knapsack 0/1 (valor máximo) → backward loop
#       (knapsack_01_max_value)
#   Frases típicas:
#       - "n objetos, cada uno con peso y valor, capacidad máxima W."
#       - "Cada objeto se puede usar como máximo una vez."
#       - "Maximizar el valor total sin superar la capacidad."
#       - "Elegir subconjunto de items para obtener el mayor beneficio posible."
#
# 7. Piden reconstruir → usar dp 2D (y opcionalmente prev[][])
#       (knapsack_01_with_reconstruction, versión LCS completa)
#   Frases típicas:
#       - Además de pedir el valor óptimo, dicen:
#           · "Imprimir qué elementos se eligieron."
#           · "Imprimir una solución óptima, no solo el valor."
#           · "Mostrar la subsecuencia / conjunto que logra el máximo."
#       - Suelen pedir:
#           · "Imprimir también el camino / conjunto / secuencia resultante."
#
# 8. Longitud + estados → dp[len][state]
#       (dp_length_state, ej. facheros / caminos por longitud)
#   Frases típicas:
#       - "Contar cuántos números / strings de longitud N cumplen ciertas reglas."
#       - "Cada dígito/estado solo puede ir seguido de algunos otros."
#       - "Número de caminos de longitud exacta N en un grafo pequeño."
#       - "Formar secuencias de longitud fija con restricciones de adyacencia."
###############################################

import sys
input = sys.stdin.readline

###############################################
# 1️⃣ DP 1D – CONTAR FORMAS (PERMUTACIONES IMPORTAN)
###############################################

# Usás esto cuando:
#   • “¿Cuántas formas hay de llegar a suma X usando estos movimientos/monedas?”
#   • El orden importa (A2, A4 Coin Combinations I).
#
# Ejemplos típicos:
#   - Dice Combinations
#   - Coin Combinations I (CSES, donde se cuentan permutaciones)

def dp_count_permutations():
    MOD = 10**9 + 7

    # ADAPTAR SEGÚN EL PROBLEMA:
    # target_sum = X (suma objetivo)
    # moves = lista de movimientos/monedas disponibles
    #
    # Ejemplo de lectura:
    # target_sum, m = map(int, input().split())
    # moves = list(map(int, input().split()))

    target_sum = 0
    moves = []

    # dp[x] = cuántas formas hay de llegar exactamente a suma x
    dp = [0] * (target_sum + 1)
    dp[0] = 1  # base: hay 1 forma de hacer 0 (no usar nada)

    for current_sum in range(1, target_sum + 1):
        ways = 0  # acumula formas para este monto
        for move in moves:
            if current_sum >= move:
                ways += dp[current_sum - move]  # formas de llegar desde current_sum - move
        dp[current_sum] = ways % MOD  # mod para evitar overflow

    print(dp[target_sum])


###############################################
# 2️⃣ DP 1D – MÍNIMO COSTO / MÍNIMO NÚMERO DE PASOS
###############################################

# Usás esto cuando:
#   • “Mínimo número de monedas para sumar X”
#   • “Mínimo costo para llegar a X”

def dp_min_cost():
    INF = 10**18

    # Ejemplo típico:
    # n, target_sum = map(int, input().split())
    # coins = list(map(int, input().split()))
    n, target_sum = 0, 0
    coins = []

    # dp[x] = mínimo número de monedas para obtener suma x
    dp = [INF] * (target_sum + 1)
    dp[0] = 0  # para sumar 0, necesito 0 monedas

    for current_sum in range(1, target_sum + 1):
        best = INF  # mejor cantidad encontrada para current_sum
        for coin in coins:
            if current_sum >= coin and dp[current_sum - coin] != INF:
                candidate = dp[current_sum - coin] + 1  # uso esta moneda + solución óptima previa
                if candidate < best:
                    best = candidate
        dp[current_sum] = best  # queda INF si no hay forma

    print(-1 if dp[target_sum] == INF else dp[target_sum])

    # Si en vez de “+1 moneda” tenés “+costo[i]”, cambiás esa parte.


###############################################
# 3️⃣ DP 1D – COMBINACIONES SIN IMPORTAR EL ORDEN (COIN COMB. II)
###############################################

# Usás esto cuando:
#   • “Cuántas formas hay de sumar X usando monedas, pero 2+3 y 3+2 cuentan como lo mismo”.
#
# Patrón clave: loop externo = monedas, loop interno = montos.

def dp_combinations_no_order():
    MOD = 10**9 + 7

    # Ejemplo típico:
    # n, target_sum = map(int, input().split())
    # coins = list(map(int, input().split()))
    n, target_sum = 0, 0
    coins = []

    # dp[x] = cuántas combinaciones (orden NO importa) suman exactamente x
    dp = [0] * (target_sum + 1)
    dp[0] = 1  # 1 forma de hacer 0: no usar monedas

    for coin in coins:
        for current_sum in range(coin, target_sum + 1):  # avanzar evita contar permutaciones
            dp[current_sum] = (dp[current_sum] + dp[current_sum - coin]) % MOD

    print(dp[target_sum])


###############################################
# 4️⃣ DP 1D – BOOLEANO: SE PUEDE O NO (SUBSET SUM)
###############################################

# Útil para:
#   • “¿Se puede lograr suma X con estos valores?”
#   • “¿Se puede llenar exactamente el peso W?”, etc.

def dp_subset_sum():
    # Ejemplo típico:
    # n, target_sum = map(int, input().split())
    # values = list(map(int, input().split()))
    n, target_sum = 0, 0
    values = []

    # possible[s] = True si es posible obtener suma s con algún subconjunto
    possible = [False] * (target_sum + 1)
    possible[0] = True

    for val in values:
        # vamos de atrás hacia adelante para no reutilizar el mismo elemento
        for s in range(target_sum, val - 1, -1):
            if possible[s - val]:
                possible[s] = True  # puedo alcanzar s agregando val a una suma previa posible

    print("YES" if possible[target_sum] else "NO")


###############################################
# 5️⃣ DP 2D – LCS (LONGEST COMMON SUBSEQUENCE)
###############################################

# Usás esto cuando:
#   • “subsecuencia común más larga” entre dos strings/secuencias.
#   • Similaridad entre dos strings.
#   • A veces sirve para problemas de edición simplificados.

def dp_lcs_length():
    # Ejemplo lectura:
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    n, m = 0, 0
    a = []
    b = []

    # dp[i][j] = longitud de LCS entre a[0..i-1] y b[0..j-1]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # caracteres iguales: extiendo LCS previo
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # descarto uno de los dos prefijos

    print(dp[n][m])

# (Si hace falta reconstrucción, usar la versión más larga que ya tenés guardada.)


###############################################
# 6️⃣ DP 1D – KNAPSACK 0/1 (SOLO VALOR MÁXIMO)
###############################################

# Usás esto cuando:
#   • “n objetos, cada uno con peso y valor, capacidad máxima W”
#   • “cada objeto se puede tomar 0 o 1 vez”
#   • “maximizar valor”.

def knapsack_01_max_value():
    # Ejemplo típico:
    # n, W = map(int, input().split())
    # weights = list(map(int, input().split()))
    # values  = list(map(int, input().split()))
    n, W = 0, 0
    weights = []
    values = []

    # dp[w] = máximo valor que puedo obtener con peso TOTAL exactamente w
    dp = [0] * (W + 1)

    for i in range(n):
        w = weights[i]
        v = values[i]
        # recorro PESOS de mayor a menor para no usar el mismo objeto más de una vez
        for current_weight in range(W, w - 1, -1):
            dp[current_weight] = max(dp[current_weight],
                                     dp[current_weight - w] + v)  # tomarlo vs no tomarlo

    # mejor valor con peso <= W
    print(max(dp))


###############################################
# 7️⃣ DP 2D – KNAPSACK 0/1 CON RECONSTRUCCIÓN
###############################################

# Cuando además querés saber qué objetos se tomaron.

def knapsack_01_with_reconstruction():
    # Ejemplo típico:
    # n, W = map(int, input().split())
    # weights = list(map(int, input().split()))
    # values  = list(map(int, input().split()))
    n, W = 0, 0
    weights = []
    values = []

    # dp[i][w] = mejor valor usando los primeros i objetos (0..i-1) con capacidad w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # no tomar objeto i-1
            if w_i <= w:
                cand = dp[i - 1][w - w_i] + v_i
                if cand > dp[i][w]:
                    dp[i][w] = cand

    best_value = dp[n][W]
    print(best_value)

    # reconstrucción: qué objetos se eligieron
    chosen = []
    i, w = n, W
    while i > 0 and w >= 0:
        if dp[i][w] == dp[i - 1][w]:
            i -= 1  # no usamos el objeto i-1
        else:
            chosen.append(i - 1)      # usamos el objeto i-1
            w -= weights[i - 1]
            i -= 1

    chosen.reverse()
    # podés imprimir índices, pesos o valores según el problema
    # print("indices:", *chosen)


###############################################
# 8️⃣ DP “POSICIÓN X ESTADO” (FACHEROS, CAMINOS POR LONGITUD)
###############################################

# Cuando tenés:
#   • una longitud N,
#   • un conjunto chico de “estados” o “dígitos”,
#   • y reglas de transición entre estados (grafo chiquito).
#
# Ejemplo: números “facheros”.

def dp_length_state():
    MOD = 10**9 + 7

    # length = cantidad de pasos/dígitos
    length = 0

    # ejemplo: estados = 0..4 (por ejemplo representan 1,3,5,7,9)
    num_states = 5

    # adj[state] = lista de estados a los que puedo ir desde 'state'
    # ADAPTAR según el problema:
    adj = [
        (1,),      # desde estado 0 puedo ir al 1
        (0, 2),    # desde 1 puedo ir a 0 o 2
        (1, 3),
        (2, 4),
        (3,)
    ]

    # dp para una longitud dada, comprimido a 1D
    # al inicio (longitud 1) hay 1 forma de terminar en cualquier estado
    dp = [1] * num_states

    if length == 1:
        print(sum(dp) % MOD)
    else:
        for _ in range(2, length + 1):
            next_dp = [0] * num_states
            for state in range(num_states):
                ways = dp[state]
                if ways == 0:
                    continue
                for to_state in adj[state]:
                    next_dp[to_state] = (next_dp[to_state] + ways) % MOD
            dp = next_dp

        answer = sum(dp) % MOD
        print(answer)

##################################################
# Fin de plantillas de DP
# Copiar solo la función que corresponda al patrón
# y adaptarla al input/enunciado del problema.
##################################################