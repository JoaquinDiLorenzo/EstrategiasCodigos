# =============== VERSION FACIL ===============

import sys
import math  # para usar la función gcd (máximo común divisor)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Variable para guardar el mejor (mayor) MCD encontrado hasta ahora
# Arrancamos en 1 porque el MCD mínimo posible entre dos números positivos es 1
best = 1

# Recorremos todos los pares (i, j) de la lista con i < j
for i in range(n):
    for j in range(i + 1, n):
        g = math.gcd(arr[i], arr[j])  # Calculamos el gcd de arr[i] y arr[j]
        best = max(best, g)

print(best)


# =============== VERSION DIFICIL ===============

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Encontramos el valor máximo del arreglo
max_val = max(arr)

# Creamos un array de frecuencias de tamaño max_val + 1
# freq[v] = cuántas veces aparece el número v en la lista
freq = [0] * (max_val + 1)

for x in arr:
    freq[x] += 1

# Recorremos los posibles candidatos a "mejor MCD" desde el más grande hacia el 1.
for d in range(max_val, 0, -1):
    count = 0  # cuántos números de arr son múltiplos de d

    # Recorremos TODOS los múltiplos de d: d, 2d, 3d, ...
    # hasta llegar a max_val.
    for multiple in range(d, max_val + 1, d):
        count += freq[multiple]  # sumamos cuántos elementos son exactamente 'multiple'

        # Si ya tenemos al menos 2 números que son múltiplos de d,
        # entonces d es MCD de algún par (o al menos divide a los dos).
        if count >= 2:
            print(d)
            sys.exit(0)   # salimos del programa: ya encontramos el máximo posible