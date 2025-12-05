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

MAX = 10**6

pri = Primos(MAX)

def main():
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        cant = upper_bound(pri.lista_primos,r) - lower_bound(pri.lista_primos,l)
        print (cant)
    
if __name__ == "__main__":
    main()