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

def es_posible(medio, k, array):
    suma = 0
    cant_sub = 1

    for x in array:
        if suma + x > medio:
            cant_sub += 1
            suma = 0
        suma += x
    return cant_sub <= k

n, k = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().strip().split()))
array = array[:n]

low_bound = max(array)
high_bound = sum(array)

check = lambda mid: es_posible(mid, k, array)

resultado = binary_search_min(low_bound, high_bound, check)

sys.stdout.write(f"{resultado}")