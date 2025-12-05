import sys 

n = int(sys.stdin.readline())

values = list(map(int, sys.stdin.readline().split()))
values = values[:n]
dp = [1] * n

if n == 0:
    sys.stdout.write("0")
    sys.exit(0)

MAX = max(values)
dp = [0] * (MAX + 1)
ans = 0

for x in values:
    cur_best = 0
    d = 1
    while d * d <= x:
        if x % d == 0:
            if best[d] > cur_best:
                cur_best = best[d]
            od = x // d
            if best[od] > cur_best:
                cur_best = best[od]
        d += 1
    cur = cur_best + 1
    if cur > best[x]:
        best[x] = cur
    if cur > ans:
        ans = cur

sys.stdout.write(str(ans))
# ...existing code...