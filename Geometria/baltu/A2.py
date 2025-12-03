import sys

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    
    def __mul__(self, escalar: float):
        return Punto(self.x * escalar, self.y * escalar)
    
    def __dot__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __xor__(self, other): # computa el producto cruzado: 
        return self.x * other.y - self.y * other.x
    
    def mod(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
t = int(sys.stdin.readline())

tests = []

for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
    tests.append((Punto(x1, y1), Punto(x2, y2), Punto(x3, y3)))

# se necesita conocer la orientacion de p3, mirando desde p1 a p2, por lo que se necesita:
# la resta entre p2 y p1 (para conocer la direccion)
# la resta entre p3 y p1 (para tomar el vector desde donde se quiere mirar)
# y se calcula el producto cruzado (xor entre el vector de direccion y el que mira)
for p1, p2, p3 in tests:
    v = p2 - p1
    w = p3 - p1
    cross = v ^ w
    if cross > 0:
        sys.stdout.write("LEFT\n")
    elif cross < 0:
        sys.stdout.write("RIGHT\n")
    else: # p3 esta sobre la recta
        sys.stdout.write("TOUCH\n")