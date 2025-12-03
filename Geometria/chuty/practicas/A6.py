from utils.PUNTO import Punto

# Este es un porbelma clasico de producto cruzado
n = int(input())
puntos = []
area2 = 0

for _ in range(n):
    a,b = map(int, input().split())
    puntos.append(Punto(a,b))

for i in range(n):
    a = puntos[i]
    b = puntos[(i+1)%n]
    area2 += (a ^ b) #Usa la funcion de _XOR_ de la clase Punto

print(abs(area2))