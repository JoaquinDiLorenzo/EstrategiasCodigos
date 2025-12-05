import sys
import math

ERR = 10**-6

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
    
    def __xor__(self, other):
        return self.x * other.y - self.y * other.x
    
    def mod(self) -> float:
        return (self.x**2 + self.y**2)**0.5

n = int(sys.stdin.readline())

coords = []

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  coords.append(Punto(x, y))

INF = float("inf")
used = [False] * n
min_sq = [INF] * n
min_sq[0] = 0

max_edge_sq = 0

if n <= 1:
    print("0.0000000000")
    sys.exit(0)

for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not used[i] and min_sq[i] < best:
            best = min_sq[i]
            u = i
    used[u] = True
    if best > max_edge_sq:
        max_edge_sq = best
    ux = coords[u].x
    uy = coords[u].y
    for v in range(n):
        if not used[v]:
            dx = ux - coords[v].x
            dy = uy - coords[v].y
            d2 = dx*dx + dy*dy
            if d2 < min_sq[v]:
                min_sq[v] = d2

res = math.sqrt(max_edge_sq)
sys.stdout.write(f"{res:.10f}")
