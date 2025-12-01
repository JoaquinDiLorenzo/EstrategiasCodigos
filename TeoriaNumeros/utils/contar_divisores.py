class Primos:
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

