import sys 
MOD = 10**9+7

n, money = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

dp = [0] * (money+1)
dp[0] = 1 # 1 forma de contar 0 

for coin in array:
    for i in range(coin, money+1):
        dp[i] = (dp[i] + dp[i- coin]) % MOD

print(dp[money])