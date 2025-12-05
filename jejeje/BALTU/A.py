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
listo = [False] * n
min_n = [INF] * n
min_n[0] = 0

max_n = 0

if n <= 1: # si hay una sola antena no hay interconexion
  print("0.0000000000")
  sys.exit(0)

for _ in range(n):
  u = -1
  mej = INF
  for i in range(n):
    if not listo[i] and min_n[i] < mej:
      mej = min_n[i]
      u = i
      
  listo[u] = True
  if mej > max_n:
    max_n = mej

  ux = coords[u].x
  uy = coords[u].y

  for v in range(n):
    if not listo[v]:
      dx = ux - coords[v].x
      dy = uy - coords[v].y

      d2 = dx*dx + dy*dy

      if d2 < min_n[v]:
        min_n[v] = d2

res = math.sqrt(max_n)
sys.stdout.write(f"{res:.10f}")
