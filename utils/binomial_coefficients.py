MAXN = 100

def binomial_coefficient(n, m):
    """
    Calcula el coeficiente binomial C(n, m), también llamado “n sobre m”,
    utilizando programación dinámica basada en el Triángulo de Pascal.

    ----------------------------------------------------------------------
    ¿Qué es el coeficiente binomial?

        C(n, m) = n! / (m! * (n - m)!)
    
    Es la cantidad de maneras de elegir m elementos distintos desde un conjunto
    de n elementos. Ejemplos:
        C(5, 2) = 10
        C(4, 1) = 4

    ----------------------------------------------------------------------
    ¿Cómo funciona esta función?

    Se construye una tabla cuadrada bc[][] de tamaño MAXN × MAXN, donde
    bc[i][j] almacenará el valor de C(i, j).

    La construcción sigue las reglas del Triángulo de Pascal:

        1. Condiciones base:
            C(i, 0) = 1         (hay 1 forma de elegir 0 elementos)
            C(i, i) = 1         (hay 1 forma de elegir todos los elementos)

        2. Relación de recurrencia:
            C(i, j) = C(i-1, j-1) + C(i-1, j)

        Esta ecuación indica que:
        - si incluimos el elemento i → contamos C(i−1, j−1)
        - si no lo incluimos        → contamos C(i−1, j)

    La función llena la tabla siguiendo esta estructura, fila por fila,
    hasta llegar a los valores de C(n, m).

    Finalmente, devuelve bc[n][m].

    ----------------------------------------------------------------------
    Limitaciones:
    - La tabla se crea nuevamente en cada llamada, lo cual es costoso
      para valores grandes o llamadas repetidas.
    - No utiliza módulo (los valores crecen rápido).
    - MAXN define el tamaño máximo permitido para n.

    ----------------------------------------------------------------------
    Parámetros:
        n (int): el número total de elementos.
        m (int): el número de elementos a elegir.

    Retorna:
        int: El valor del coeficiente binomial C(n, m).

    Ejemplos:
        binomial_coefficient(5, 2) → 10
        binomial_coefficient(6, 3) → 20
    """
    
    bc = [[0] * (MAXN) for _ in range(MAXN)]

    # casos base
    for i in range(n + 1):
        bc[i][0] = 1
        bc[i][i] = 1

    # construir la tabla
    for i in range(1, n + 1):
        for j in range(1, i):
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j]

    return bc[n][m]
