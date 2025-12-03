import sys 
import bisect

n, a, b = map(int, sys.stdin.readline().split())

factores = list(map(int, sys.stdin.readline().strip().split()))
factores = factores[:n]

factores_ordenados = sorted(factores)

for p in factores:
    # depredadores
    # lower_bound(x+b) - lower_bound(x+a)
    dep = bisect.bisect_left(factores_ordenados, p+b) - \
          bisect.bisect_left(factores_ordenados, p+a)
    
    # presas
    # upper_bound(x-a) - upper_bound(x-b)
    pres = bisect.bisect_right(factores_ordenados, p-a) - \
           bisect.bisect_right(factores_ordenados, p-b)

    sys.stdout.write(f"{dep} {pres}\n")