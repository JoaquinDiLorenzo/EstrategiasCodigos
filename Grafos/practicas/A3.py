from utils.DSU import DSU

N,M = map(int, input().split())
dsu = DSU(N)

for _ in range(M):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    dsu.union(a,b)

# Saco los representantes para luego evaluar las conexiones minimas
representantes = []
for i in range(N):
    if dsu.find(i) == i:
        representantes.append(i)

print(len(representantes)-1) #Imprimo la cantidad de conexiones faltantes
for i in range(0, len(representantes)-1): #Conecto los representnas vecinos (obtengo toda la ciudad conectada)
    a = representantes[i] + 1 
    b = representantes[i+1] + 1
    print(a,b)
