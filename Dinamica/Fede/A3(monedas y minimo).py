import sys

INF = 10**8
n, money = map(int, input().split())
array = list(map(int, input().split()))

dp = [INF] * (money + 1) # ya que pide el minimo 
dp[0] = 0

for i in range(1, money+1):
    for j in array: # 1 5 7
        if (i - j >= 0):
            dp[i] = min(dp[i], dp[i-j]+1) # moneda anterior + la moneda actual
            
print(-1 if dp[money] == INF else dp[money])
