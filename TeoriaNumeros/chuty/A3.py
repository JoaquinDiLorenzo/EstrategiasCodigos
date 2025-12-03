MAXN = 100
MOD = (10 ** 9)+7

def binomial_coefficient(n, m):
    
    bc = [[0] * (MAXN) for _ in range(MAXN)]

    # casos base
    for i in range(n + 1):
        bc[i][0] = 1
        bc[i][i] = 1

    # construir la tabla
    for i in range(1, n + 1):
        for j in range(1, i):
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j]

    return bc[n][m]

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    res = binomial_coefficient(a,b)
    print(res % MOD)