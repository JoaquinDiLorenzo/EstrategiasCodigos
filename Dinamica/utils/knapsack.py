# ======================================================================
#  KNAPSACK 0/1 – IMPLEMENTACIÓN 1D
# ======================================================================
#  Objetivo:
#     Dado un conjunto de objetos, cada uno con peso y valor, y una
#     capacidad máxima, obtener el valor máximo posible sin repetir
#     objetos (cada objeto se toma 0 o 1 vez).
#
#  Idea general:
#     dp[w] = mejor valor que puedo obtener usando algunos objetos y
#             con capacidad máxima w.
#
#     Cuando proceso un objeto de peso wi y valor vi:
#         Recorro w desde max_weight → wi
#         Esto garantiza que el objeto NO se use más de una vez.
#
#     Relación:
#         dp[w] = max(dp[w], dp[w - wi] + vi)
#
#     Si recorriera w de menor a mayor, estaría permitiendo reutilizar
#     el mismo objeto múltiples veces (eso sería Unbounded Knapsack).
#
# ======================================================================

def knapsack_01(weights, values, max_weight):
    """
    Resuelve el knapsack 0/1 clásico usando un DP unidimensional.

    Parámetros:
        weights     lista de pesos de los objetos
        values      lista de valores de los objetos
        max_weight  capacidad máxima de la mochila

    Retorna:
        valor máximo que se puede obtener sin exceder el peso.
    """

    n = len(weights)
    dp = [0] * (max_weight + 1)

    # Recorremos cada objeto una sola vez
    for i in range(n):
        wi = weights[i]
        vi = values[i]

        # Recorremos pesos de atrás hacia adelante.
        # Esto es CRÍTICO para forzar 0/1 knapsack.
        for w in range(max_weight, wi - 1, -1):
            # O no lo tomo (dp[w]) o lo tomo (dp[w - wi] + vi)
            dp[w] = max(dp[w], dp[w - wi] + vi)

    return dp[max_weight]


# ======================================================================
#  CUÁNDO USAR ESTE ALGORITMO
# ======================================================================
#  Usar esta versión (1D, de atrás hacia adelante) cuando:
#     - Cada objeto puede tomarse como máximo UNA vez.
#     - Solo importa el valor máximo acumulado.
#     - Necesitás mejor rendimiento en memoria (O(W)).
#
#  No usar esta versión cuando:
#     - Los objetos pueden repetirse infinitamente → usar "Unbounded Knapsack".
#     - Tenés límites de cantidad para cada objeto → variante bounded.
#
#  Tipos de problemas donde se aplica:
#     - Selección de tareas, inversiones, cargas, subconjuntos óptimos.
#     - Cualquier situación donde algo "ocupa peso" y "da valor" y
#       cada elemento puede utilizarse 0 o 1 vez.
#
# ======================================================================