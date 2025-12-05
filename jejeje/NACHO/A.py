
# Un colegio quiere instalar una red WI-FI en las 𝑁
#  aulas y para ello, se piensa colocar una antena en cada una de ellas. Cada antena tiene un radio máximo de alcance. Diremos que dos antenas están interconectadas si su radio de alcance es mayor o igual a la distancia que se encuentran entre sí, o, existe un camino de antenas intermedias en las cuales las distancias entre antenas consecutivas del camino no superan el radio de alcance.

# Para facilitar la compra de las antenas, se van a elegir el mismo modelo para todas, por lo que todas tendrán el mismo radio de alcance.

# Dado el plano con las coordenadas geográficas (𝑥𝑖,𝑦𝑖)
#  de la ubicación de cada antena, determinar el menor valor de radio de alcance posible de manera tal que toda la red quede interconectada. La respuesta será considerada correcta si el error relativo en su resultado y el del juez es menor a 10−6
# .

# Diremos que la red queda totalmente interconectada si para cada par de antenas existe una conexión ya sea directa, o indirectamente a través de otras antenas.

# Input
# En la primera línea estará 𝑁
# , el número de antenas por instalar. En las siguientes 𝑁
#  líneas encontrarán dos enteros (𝑥𝑖,𝑦𝑖)
# , las coordenadas de cada antena.

# Versión Fácil (15 Puntos)

# Las aulas se encuentran todas en un mismo pasillo. La ubicación se las antenas se modela de forma tal que todas queden en una misma recta, sobre el eje 𝑥
#  (es decir, las coordenadas 𝑦𝑖
#  de cada antena será cero.

#La version facil siempre el radio necesario va a ser igual a la distancia maxima entre antenas.

# Versión Difícil (25 Puntos)

# Las aulas se encuentran distribuidas en un plano.

# 1≤𝑁≤1000

# −106≤𝑥𝑖,𝑦𝑖≤106

# import sys

# class Punto:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
        
#     def __add__(self, other):
#         return Punto(self.x + other.x, self.y + other.y)
    
#     def __sub__(self, other):
#         return Punto(self.x - other.x, self.y - other.y)
    
#     def __mul__(self, escalar: float):
#         return Punto(self.x * escalar, self.y * escalar)
    
#     def __dot__(self, other):
#         return self.x * other.x + self.y * other.y
    
#     def __xor__(self, other): # computa el producto cruzado: 
#         return self.x * other.y - self.y * other.x
    
#     def mod(self) -> float:
#         return (self.x**2 + self.y**2)**0.5


# MAX = 10**6+1

def main():
    n = int(input())

    # antenas = []
    puntosx =[]
    for _ in range(n):
        x, y = map(int, input().split())
        # antenas.append(Punto(x, y))
        puntosx.append(x)
        max = -1
        
    puntosx.sort()
        
    for i in range(n-1):
        dis = abs(puntosx[i] - puntosx[i+1])
        if dis>max:
            max=dis

    print (max)
                

if __name__ == "__main__":
    main()