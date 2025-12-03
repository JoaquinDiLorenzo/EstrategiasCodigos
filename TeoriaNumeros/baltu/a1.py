import sys

MOD = 10**9 + 7

# computa un numero exponenciado en binario, mucho mas eficiente
def modular_exp_iter(x, y):
    res = 1
    while (y != 0):
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return res

n = int(sys.stdin.readline())

values = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    values.append((a, b))

for a, b in values:
    sys.stdout.write(f"{modular_exp_iter(a, b)}\n")