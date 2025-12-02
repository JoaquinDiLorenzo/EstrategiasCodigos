import sys

def binary_search_min(low, high, check):
    ans = high 
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def se_puede_producir(seconds):
        products = 0
        for k in times:
            products += seconds // k
            if products >= t: # optimiza
                return True
        return products >= t

n, t = map(int, sys.stdin.readline().split())

times = list(map(int, sys.stdin.readline().strip().split()))
times = times[:n]
times = sorted(times)

low_bound = 1
high_bound = min(times) * t

result = binary_search_min(low_bound, high_bound, se_puede_producir)

sys.stdout.write(f"{result}\n")