from sys import stdin

MOD = 10**9+7

adj = [
    (1,), # 1 con 3
    (0, 2), # 3 con 1 y 5
    (1, 3), # 5 con 3 y 7
    (2, 4), # 7 con 5 y 9
    (3,) # 9 con 7
]

dp = [1, 1, 1, 1, 1] # dp[1][cualquiera] siempre es 1

digits = int(stdin.readline())

if digits != 1:
    for _ in range(2, digits + 1): # longitudes
        next_dp = [0, 0, 0, 0, 0] # inicializa las adyacencias (longitudes 1 = 0)
        for i in range(5): # recorre los digitos 
            ways = dp[i] # cuantas formas hay de terminar en el digito i en la longitud
            if ways == 0:
                continue
            for j in adj[i]: # se extienden las formas que terminaban en i agregando el digito j
                next_dp[j] = (next_dp[j] + ways) % MOD
        dp = next_dp # dp es la longitud nueva
print(sum(dp) % MOD)