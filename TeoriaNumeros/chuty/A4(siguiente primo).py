# Como no podemos hacer la criba de 10 ^ 12, lo qu ehacemos es hacerla de 10 ^ 6 (aplicandole raiz cuadrada a 12)
# El codiog funcion igual por la siguiente regla matemtica -> Si ningún primo hasta Sqrt(x) divide a X, entonces forzosamente X es primo.

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

n = int(input())

for _ in range(n):
    t = int(input())
    num = t+1
    while not prim.test_primalidad(num):
        num += 1
    print(num)