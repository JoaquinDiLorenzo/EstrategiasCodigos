import sys
sys.setrecursionlimit(10000)  # Aumentar límite de recursión

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[-1]*(m+1) for i in range(n+1)]
prev = [[(-1,-1)]*(m+1) for i in range(n+1)]

# Solucion utilizando tecnica Top-Down

def LCS(i,j,a,b,dp,prev):
    if i == 0 or j == 0: 
        dp[i][j] = 0
        prev[i][j] = (0,0)
        return 0
    if dp[i][j] != -1: 
        return dp[i][j]
    
    # Calcular recursivamente
    up = LCS(i-1,j,a,b,dp,prev)
    left = LCS(i,j-1,a,b,dp,prev)
    diag = LCS(i-1,j-1,a,b,dp,prev)
    
    # Determinar el mejor valor
    dp[i][j] = max(up, left)
    if up >= left:
        prev[i][j] = (i-1,j)
    else:
        prev[i][j] = (i,j-1)
    
    # Verificar si coinciden los elementos
    if a[i-1] == b[j-1] and diag + 1 > dp[i][j]:
        dp[i][j] = diag + 1
        prev[i][j] = (i-1,j-1)
    
    return dp[i][j]

LCS(n,m,a,b,dp,prev)
print(dp[n][m])

# Reconstruimos el LCS
lcs = []
estadoActual = (n,m)
while estadoActual[0] > 0 and estadoActual[1] > 0:
    x,y = estadoActual
    sx,sy = prev[x][y]
    # Verificamos que los índices sean válidos antes de continuar
    if sx < 0 or sy < 0:
        break
    if sx == x-1 and sy == y-1:
        lcs.append(a[sx])
        # Aca podemos pushear tambien b[sy] porque serian el mismo elemento
    estadoActual = (sx,sy)
lcs.reverse()

for x in lcs:
    print(x, end = ' ')
    
print() 