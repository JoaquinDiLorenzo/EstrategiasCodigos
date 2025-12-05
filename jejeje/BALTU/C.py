import sys
import bisect

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
        
        for i in range(n + 1):
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

q = int(sys.stdin.readline())

values = []
max_r = -1

for _ in range(q):
  l, r = map(int, sys.stdin.readline().split())
  values.append((l, r))
  if r > max_r:
    max_r = r

p = Primos(max_r) # una sola vez

for l, r in values:
  left = bisect.bisect_left(p.lista_primos, l)
  right = bisect.bisect_right(p.lista_primos, r)
  sys.stdout.write(f"{right - left}\n")