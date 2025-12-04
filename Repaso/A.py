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
    
MAX = 10 ** 6
prim = Primos(MAX)

def contar_primos_distintos(x):
    cnt = 0
    tmp = x

    for p in prim.lista_primos:
        if p * p > tmp:
            break
        if tmp % p == 0:
            cnt += 1
            while tmp % p == 0:
                tmp //= p

    if tmp > 1:
        cnt += 1

    return cnt

n = int(input())

for _ in range(n):
    number = int(input())
    print(contar_primos_distintos(number))

'''
La función contar_primos_distintos(x) calcula cuántos factores primos distintos tiene un número.
Para hacerlo usa la lista de primos generada por la criba:

Recorre los primos p y se detiene cuando p² > x, porque si queda algún resto mayor que 1, ese resto es primo.

Para cada primo p, si p divide a x, lo cuenta una sola vez (factor primo distinto) y elimina todas sus copias dividiendo repetidamente.

Al final, si el número reducido quedó mayor que 1, significa que es un primo grande y se suma un factor más.

Este método permite factorizar números hasta 10¹² usando solo los primos precomputados hasta 10⁶.
'''
