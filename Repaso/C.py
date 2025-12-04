MAX = 10**6

# Construir la cadena de manera correcta (join sobre un generador)
numeros = ''.join(str(i) for i in range(1, MAX+1))

q = int(input())

for _ in range(q):
    index = int(input())
    print(numeros[index-1])