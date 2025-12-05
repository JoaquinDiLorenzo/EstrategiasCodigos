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
    
MAX_NUM = 10 ** 6

prim = Primos(MAX_NUM)
    
def contar_divisores(x):
     
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

n = int(input())

for _ in range(n):
    num = int(input())
    print(contar_divisores(num))