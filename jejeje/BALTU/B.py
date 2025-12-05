import sys 

n = int(sys.stdin.readline())

values = list(map(int, sys.stdin.readline().split()))
values = values[:n]
dp = [1] * n
 
for i in range(n-1, -1, -1): # se recorre de derecha a izquierda
  for j in range(i+1, n): # se recorre desde el que estoy parado hacia adelante, viendo posibilidades
    if values[j] > values[i] and values[i] // values[j] == 0:
      dp[i] = max(dp[i], dp[j]+1) # se almacena el maximo elemento que seguiria el camino
 
sys.stdout.write(f"{max(dp)}")