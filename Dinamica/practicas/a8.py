from sys import stdin 

objects, max_weight = map(int, stdin.readline().split())
objects_weight = list(map(int, stdin.readline().split()))
objects_price = list(map(int, stdin.readline().split()))

dp = [-1] * (max_weight+1)
dp[0] = 0

for i in range(objects):
    new_dp = dp[:]
    for j in range(objects_weight[i], max_weight + 1):
        if dp[j - objects_weight[i]] != -1:
            new_dp[j] = max(new_dp[j], dp[j - objects_weight[i]] + objects_price[i])
    dp = new_dp

print(max(dp))