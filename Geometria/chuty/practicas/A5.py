from utils.PUNTO import Punto
from utils.INTERSECCION import segments_intersect

t = int(input())

for _ in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())

    if segments_intersect(Punto(x1,y1), Punto(x2,y2), Punto(x3,y3), Punto(x4,y4)):
        print("YES")
    else:
        print("NO")