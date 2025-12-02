from sys import stdin 

MOD = 10**9+7

coins_number, money = map(int, stdin.readline().split())
coins = list(map(int, stdin.readline().split()))
coins = [c for c in coins if c <= money]
coins.sort()

dp = [0] * (money+1)
dp[0] = 1

for i in range(1, money+1):
    total = 0
    for coin in coins: # coins esta ordenado, se corta cuando coin > i
        if coin > i:
            break
        total += dp[i-coin]
    dp[i] = total % MOD

print(dp[money])