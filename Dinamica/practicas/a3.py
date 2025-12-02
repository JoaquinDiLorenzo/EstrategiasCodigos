from sys import stdin 

coins_number, money = map(int, stdin.readline().split())
coins = set(map(int, stdin.readline().split()))

MAX = money + 1 # no se necesita mas monedas que la cantidad de dinero
dp = [MAX] * (money + 1) 
dp[0] = 0 # para formar 0 hacen falta 0 monedas

# para encontrar la mejor solucion para cada suma:
for coin in coins: 
    for i in range(coin, money+1): # para cada suma desde la moneda hasta el conteo total
        new = dp[i - coin] + 1 # posible mejor solucion
        if new < dp[i]: # si es mejor solucion
            dp[i] = new # como se puede formar i - coin, se puede formar i agregando esa moneda

print(dp[money] if dp[money] != MAX else -1) 