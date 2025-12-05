class Primos:
    """
    Clase diseñada para precomputar información relacionada con números primos
    hasta un límite dado n, utilizando una variación de la Criba de Eratóstenes.

    La clase construye tres estructuras fundamentales:

        1. es_primo[i]:
           Booleano que indica si i es un número primo.
           - es_primo[i] = True  si i es primo
           - es_primo[i] = False si i es compuesto o i < 2

        2. min_primo[i]:
           El menor primo que divide al número i.
           - min_primo[i] = 0 para números primos o para i = 0 y 1.
           - Si i es compuesto, min_primo[i] es el menor prime factor (spf).

           Esto permite factorizar números en tiempo O(log n).

        3. lista_primos:
           Lista con todos los números primos generados por la criba, en orden
           creciente. Útil para:
               - test de primalidad
               - factorizar números mayores que n
               - recorrer primos rápidamente

    ----------------------------------------------------------------------
    ¿Cómo funciona la criba?

    La función criba(n):
        - Inicializa es_primo en True.
        - Marca 0 y 1 como no primos.
        - Recorre todos los números desde 2 hasta n.
            • Si es_primo[i] sigue siendo True, entonces i es primo.
              Se agrega a lista_primos.
            • Luego, se recorre j = i*i, i*(i+1), ... y se marcan como compuestos.
              Para cada j:
                - es_primo[j] = False
                - min_primo[j] = i  (primer primo que lo divide)

    De esta manera, obtenemos:
        - Una criba clásica de primos
        - Un spf array (smallest prime factor)
        - Una lista explícita de todos los primos hasta n

    Esto permite factorizaciones rápidas como:
        x = p1^a1 * p2^a2 * ...
    aplicando sucesivos min_primo[x].

    ----------------------------------------------------------------------
    Test de primalidad extendido:

    El método test_primalidad(x) funciona así:

        - Si x <= n:
              Devuelve directamente es_primo[x] en O(1).
        - Si x > n:
              Lo prueba dividiéndolo por todos los primos precalculados ≤ n.
              Si alguno divide a x → x no es primo.
              Si ninguno divide a x → x es primo.

    Esto permite testear primos hasta valores muy grandes (~10^12 o más)
    si la criba se construyó hasta sqrt(x).

    ----------------------------------------------------------------------
    Usos típicos de esta clase:

    - Factorización rápida de muchos números ≤ n
    - Cálculo de cantidad de divisores
    - Cálculo de funciones aritméticas (φ(n), σ(n), etc.)
    - Resolver problemas que requieren:
        • primalidad en O(1)
        • factorización en O(log n)
        • generar primos
    - Test de primalidad para números grandes usando división por primos pequeños

    ----------------------------------------------------------------------
    Complejidad:

        Construcción de criba:
            O(n log log n)

        Test primalidad para x <= n:
            O(1)

        Test primalidad para x > n:
            O(π(n)) ≈ n / log n

        Factorización usando min_primo:
            O(log n)

    ----------------------------------------------------------------------

    En resumen, esta clase es una estructura completa para manejo eficiente
    de números primos y factorización, útil en problemas de teoría de números
    en programación competitiva.
    """
    
    def __init__(self, n):
        self.lista_primos = []  # lista de números primos
        self.min_primo = []  # menor primo que divide a i
        self.es_primo = []  # True si es primo
        self.criba(n)
    
    def criba(self, n):
        self.min_primo = [0] * (n + 1)
        self.es_primo = [True] * (n + 1)  # En principio son todos primos
        self.es_primo[0] = self.es_primo[1] = False  # El 0 y 1 no son primos
        
        for i in range(2, n + 1):
            if not self.es_primo[i]:
                continue
            self.lista_primos.append(i)
            j = i * i
            while j <= n:
                if self.es_primo[j]:
                    self.es_primo[j] = False
                    self.min_primo[j] = i
                    # i es el menor primo que divide a j
                j += i
    
    def test_primalidad(self, x):
        if x < len(self.es_primo):
            return self.es_primo[x]
        
        # Asegurarse que estén hallados todos los primos
        # menores o igual a sqrt(x) en la criba
        for p in self.lista_primos:
            if x % p == 0:
                return False
        return True
    
MAX = 10**6

prim = Primos(MAX)
    
def contar_divisores(x):
    """
    Calcula la cantidad de divisores positivos del número entero x.

    Utiliza la información precalculada en el objeto global `prim` de la clase `Primos`,
    que contiene, para cada número hasta MAX, el menor primo que lo divide
    en el arreglo `prim.min_primo`.

    ----------------------------------------------------------------------
    Idea matemática:

        Si la factorización en primos de x es:
            x = p1^a1 * p2^a2 * ... * pk^ak

        entonces la cantidad de divisores positivos de x es:
            (a1 + 1) * (a2 + 1) * ... * (ak + 1)

        Ejemplo:
            x = 12 = 2^2 * 3^1
            cantidad de divisores = (2+1) * (1+1) = 3 * 2 = 6
            divisores: 1, 2, 3, 4, 6, 12

    ----------------------------------------------------------------------
    Cómo funciona el algoritmo:

    1. Caso base:
        - Si x == 1, se devuelve 1 porque el único divisor de 1 es él mismo.

    2. Inicializa `total = 1`, que irá acumulando el producto de (exponente+1)
       para cada primo en la factorización.

    3. Mientras x > 1:
        - Se toma `p = prim.min_primo[x]`, el menor primo que divide a x.
        - Si `p == 0`, significa que `x` es primo (no fue marcado como compuesto
          en la criba):
              • En ese caso, la factorización restante es x^1
              • Por lo tanto, se multiplican los divisores por (1+1) = 2
              • Se retorna `total * 2` directamente.

        - Si `p != 0`, se cuenta cuántas veces `p` divide a x:
              • Se repite: x //= p y se incrementa `exp` mientras x sea múltiplo de p.
              • Al finalizar, `exp` es el exponente de p en la factorización.

        - Se actualiza `total *= (exp + 1)` para incorporar ese primo p.

    4. Cuando x llega a 1, se han procesado todos los factores primos,
       y `total` contiene la cantidad total de divisores de x original.

    Parámetros:
        x (int): número entero positivo del que se desea conocer la cantidad de divisores.

    Retorna:
        int: cantidad de divisores positivos de x.
    """
    
    if x == 1:
        return 1

    total = 1
    while x > 1:
        p = prim.min_primo[x]
        if p == 0:
            # x es primo
            return total * 2
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
        total *= (exp + 1)
    return total


# ====================================================


'''
Funcion para obtener el sigueinte primo
'''
def proximo_primo(num):
    num += 1
    while not prim.test_primalidad(num):
        num += 1
    return num

# Como no podemos hacer la criba de 10 ^ 12, lo que hacemos es hacerla de 10 ^ 6 (aplicandole raiz cuadrada a 12)
# El codigo funciona igual por la siguiente regla matematica -> Si ningún primo hasta Sqrt(x) divide a X, entonces forzosamente X es primo.


# ====================================================


def contar_primos_distintos_factorizacion(x: int) -> int:
    """
    Devuelve la cantidad de factores primos *distintos* de x.
    Ejemplo: x = 60 = 2^2 * 3 * 5  -> retorna 3 (porque los primos distintos son 2, 3 y 5).
    Esta función funciona bien incluso si x llega hasta ~10^12,
    siempre que 'prim' tenga todos los primos hasta sqrt(x) (por eso usamos MAX = 10^6).
    """
    cnt = 0          # contador de primos distintos
    tmp = x          # copia de x que vamos a ir dividiendo

    # Recorremos los primos precomputados
    for p in prim.lista_primos:
        # Si p^2 > tmp, ya no hace falta seguir:
        # Si quedara algún divisor primo de tmp, tendría que ser <= sqrt(tmp).
        # Si p^2 > tmp, significa que no hay más divisores pequeños.
        if p * p > tmp:
            break

        # Si p divide a tmp, entonces p es un factor primo de x
        if tmp % p == 0:
            cnt += 1          # contamos este primo una sola vez

            # Dividimos tmp por p hasta eliminar por completo todas las apariciones de p
            # (así no lo contamos más de una vez)
            while tmp % p == 0:
                tmp /= p

    # Al terminar el bucle:
    # Si tmp > 1, significa que lo que quedó en tmp es un primo > 1 (un "primo grande"),
    # porque ya le sacamos todos los factores primos pequeños (<= sqrt(x)).
    if tmp > 1:
        cnt += 1

    return cnt