# =============== VERSION FACIL ===============

MAX = 10**6

# Construir la cadena de numeros hasta 10^6 (join sobre un generador)
numeros = ''.join(str(i) for i in range(1, MAX+1))

q = int(input())

for _ in range(q):
    index = int(input())
    print(numeros[index-1]) # index-1 para acomodar por el 0


# =============== VERSION DIFICIL ===============


import sys

q = int(sys.stdin.readline())

def digit_at(k):

    # 1) encontrar el bloque de dígitos
    digits = 1
    count = 9   # cantidad de números de "digits" dígitos

    while k > digits * count:
        k -= digits * count
        digits += 1
        count *= 10  # ahora count será 90, 900, 9000...

    # 2) dentro del bloque:
    #   cada número tiene "digits" dígitos
    #   ¿qué número contiene al dígito buscado?
    index = (k - 1) // digits   # posición del número dentro del bloque
    number = 10**(digits - 1) + index

    # 3) ¿qué dígito dentro del número?
    digit_index = (k - 1) % digits

    return str(number)[digit_index]


for _ in range(q):
    k = int(sys.stdin.readline())
    print(digit_at(k))