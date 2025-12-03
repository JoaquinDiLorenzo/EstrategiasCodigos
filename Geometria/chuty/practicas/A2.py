from utils.PUNTO import Punto
from utils.VECTORES import orient

t = int(input())

for _ in range(t):
    x1,y1,x2,y2,x3,y3 = map(int, input().split())
    
    value = orient(Punto(x1,y1),Punto(x2,y2), Punto(x3,y3))

    if value > 0:
        print("LEFT")
    elif value < 0:
        print("RIGHT")
    else:
        print("TOUCH")