import sys 

MAX = 1000
MOD = 10**9 + 7

def binomial_coefficient(n):
    # calcula todos los binomiales hasta n
    bc = [[0] * (MAX+1) for _ in range(MAX+1)]

    # casos base
    for i in range(n + 1):
        bc[i][0] = 1
        bc[i][i] = 1

    # construir la tabla
    for i in range(2, n + 1):
        for j in range(1, i):
            bc[i][j] = (bc[i - 1][j - 1] + bc[i - 1][j]) % MOD

    return bc

bc = binomial_coefficient(MAX) # se calcula una sola vez

n = int(sys.stdin.readline())

values = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    values.append((a, b))

for a, b in values:
    sys.stdout.write(f"{bc[a][b]}\n")