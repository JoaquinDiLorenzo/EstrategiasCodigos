MOD = 10**9 + 7

def modular_exp_iter(x, y):
    
    res = 1
    while (y != 0):
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return res

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    print(modular_exp_iter(a,b))