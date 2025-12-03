from utils.PUNTO import Punto
from utils.LINEA import line_relation
#No pasa codeforces pero está bien

t = int(input())

for _ in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())

    relation, intersection = line_relation(Punto(x1,y1), Punto(x2,y2), Punto(x3,y3), Punto(x4,y4))

    if intersection:
        print(f"{intersection.x:.10f} {intersection.y:.10f}")
    else:
        print(relation)

