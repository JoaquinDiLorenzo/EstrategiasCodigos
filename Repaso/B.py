import sys
import math  # para usar gcd

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

best = 1

for i in range(n):
    for j in range(i+1, n):
        best = max(best, math.gcd(arr[i], arr[j]))

print(best)