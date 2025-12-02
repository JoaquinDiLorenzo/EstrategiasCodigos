MOD = 10**9 + 7

def modular_exp_iter(x, y):
    """
    Calcula (x^y) mod MOD utilizando exponenciación binaria iterativa.

    ----------------------------------------------------------------------
    ¿Para qué sirve esta función?

    Necesitamos calcular x^y (x elevado a la potencia y), pero cuando y es grande
    —por ejemplo, y puede tener valores del orden de 10^12 o más— sería
    completamente inviable multiplicar x por sí mismo y veces.

    La exponenciación binaria (o "binary exponentiation") permite calcular
    potencias en tiempo O(log y), en lugar de O(y). Esto es esencial en
    programación competitiva, criptografía y problemas modulares.

    Además, trabajar con módulo (MOD) evita números gigantes y mantiene
    todos los valores dentro del rango de enteros eficientes en Python.

    ----------------------------------------------------------------------
    Idea del algoritmo:

    Toda potencia y puede descomponerse en su representación binaria.
    Por ejemplo:

        y = 13 = (1101)_2 → x^13 = x^8 * x^4 * x^1

    Entonces:
        - Recorremos los bits de y mientras lo dividimos por 2.
        - Cada vez que el bit actual es 1 (y es impar), multiplicamos al resultado.
        - Cada paso eleva x al cuadrado (para avanzar al siguiente bit).

    De esta forma, reducimos el problema exponencialmente:
        x^y → x^(y/2) → x^(y/4) → ...

    ----------------------------------------------------------------------
    Cómo funciona el ciclo:

        res = 1          # acumulador de la potencia
        mientras y > 0:
            si y es impar:                     # bit menos significativo es 1
                res = (res * x) mod MOD

            x = (x * x) mod MOD                # elevar base al cuadrado
            y = y // 2                         # desplazar bits (y >> 1)

    Cuando y llega a 0, 'res' contiene x^y mod MOD.

    ----------------------------------------------------------------------
    Propiedades importantes:

    - Tiempo de ejecución: O(log y)
    - Memoria: O(1)
    - Funciona incluso para exponentes extremadamente grandes
    - Es seguro con módulo (MOD) para evitar overflow
    - Usado en:
        • aritmética modular
        • combinatoria (cálculo de inversas modulares)
        • teoría de números
        • criptografía (RSA, Diffie-Hellman)
        • algoritmos de CSES y Codeforces

    ----------------------------------------------------------------------
    Parámetros:
        x (int): base de la potencia
        y (int): exponente (entero no negativo)

    Retorna:
        int: (x^y) mod MOD

    Ejemplos:
        modular_exp_iter(2, 10) → 1024 mod MOD = 1024
        modular_exp_iter(3, 0)  → 1
        modular_exp_iter(5, 3)  → 125
    """
    res = 1
    while (y != 0):
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return res