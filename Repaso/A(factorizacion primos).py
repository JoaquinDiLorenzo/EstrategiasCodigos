# ========== VERSION DIFICIL ==========

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
    
# ============================================
    
MAX = 10 ** 6
prim = Primos(MAX)

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

n = int(input())

for _ in range(n):
    number = int(input())
    print(contar_primos_distintos_factorizacion(number))
