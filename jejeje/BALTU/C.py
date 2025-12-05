import sys

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
    
def prefijos(max_n):
    es_primo = [True] * (max_n + 1)
    if max_n >= 0:
        es_primo[0] = False
    if max_n >= 1:
        es_primo[1] = False
    lim = int(max_n**0.5) + 1
    for i in range(2, lim):
        if es_primo[i]:
            step = i
            start = i * i
            for j in range(start, max_n + 1, step):
                es_primo[j] = False

    prefix = [0] * (max_n + 1)
    cnt = 0
    for i in range(max_n + 1):
        if es_primo[i]:
            cnt += 1
        prefix[i] = cnt
    return prefix

q = int(sys.stdin.readline())

values = []
max_r = 0

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    values.append((l, r))
    if r > max_r:
        max_r = r

prefix = prefijos(max_r)

out_lines = []
for l, r in values:
    left = prefix[l-1] if l-1 >= 0 else 0
    out_lines.append(str(prefix[r] - left))

sys.stdout.write("\n".join(out_lines))