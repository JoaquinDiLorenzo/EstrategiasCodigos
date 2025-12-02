from utils.PUNTO import Punto
from utils.VECTORES import orient

N = int(input())
puntos = []

for _ in range(N):
    x,y = map(int, input().split())
    puntos.append(Punto(x,y))

orientacion = 0 
convexo = True

for i in range(N):
    a = puntos[i]
    b = puntos[(i+1) % N]
    c = puntos[(i+2) % N]

    value = orient(a,b,c)
    if value == 0: # Puntos colineales no cambian curvatura
        continue

    if orientacion == 0: # El primer giro, define la curvatura
        orientacion = value
        continue
    
    if (orientacion > 0 and value < 0) or (orientacion < 0 and value > 0):
        convexo=False
        break

print("YES" if convexo else "NO")
    
        
    
    


