import sys 

n = int(sys.stdin.readline())

values = list(map(int, sys.stdin.readline().split()))

if n == 0: # caso base
  sys.stdout.write("0")
  sys.exit(0)

MAX = max(values)
dp = [0] * (MAX + 1)
res = 0

for value in values:
    mej = 0
    mult = 1

    while mult * mult <= value:
      if value % mult == 0:
        # si mult es divisor del valor en que se esta
        if dp[mult] > mej:
          mej = dp[mult]

        # divisor extra
        div = value // mult

        if dp[div] > mej:
          mej = dp[div]
                
      mult += 1

    cand = mej + 1

    # actualizacion
    if cand > dp[value]:
        dp[value] = cand
    if cand > res:
        res = cand

sys.stdout.write(f"{res}")