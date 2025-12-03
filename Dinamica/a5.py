from sys import stdin 

MOD = 10**9+7

coins_number, money = map(int, stdin.readline().split())
coins = list(map(int, stdin.readline().split()))

dp = [0] * (money+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, money+1):
        dp[i] = (dp[i] + dp[i-coin]) % MOD

print(dp[money])