import math

from utils.PUNTO import Punto
from utils.VECTORES import dist2

def closest_points(puntos):
    n = len(puntos)
    min_d2 = float('inf') #Saco el valor inf de float

    for i in range(n):
        for j in range(i+1,n):
            # Saco el dist2(sin raiz), ya que solo neceisto comparar disntancias
            d2 = dist2(puntos[i],puntos[j]) 
            if d2 < min_d2:
                min_d2 = d2
    
    return math.sqrt(min_d2) # Para devolver la disntacia real, debo aplicar la raiz cuadrada.

N = int(input())
puntos = []

for _ in range(N):
    x,y = map(float, input().split())
    puntos.append(Punto(x,y))

dist = closest_points(puntos)

print(f"{dist:.10f}") #Imprimo el numero y sus 10 decimales.