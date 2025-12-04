import sys 
MOD = 10**9+7

n, money = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort() # para poder usar el break en el for 

dp = [0] * (money+1)
dp[0] = 1 # 1 forma de contar 0 

for i in range(1, money+1):
    for j in array:
        if i - j >=0: 
            dp[i] = (dp[i] + dp[i-j]) % MOD
        else:
            break

print(dp[money])