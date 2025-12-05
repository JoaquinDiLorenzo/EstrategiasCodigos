import sys 
import bisect

# Leemos n, a, b
# n = cantidad de animales
# a = diferencia mínima para que un animal pueda depredar a otro
# b = diferencia a partir de la cual el depredador considera a la presa "demasiado débil"
n, a, b = map(int, sys.stdin.readline().split())

factores = list(map(int, sys.stdin.readline().strip().split()))
factores = factores[:n]  # aseguramos tamaño correcto

# Ordenamos todos los factores para binary search
# el arreglo original se mantiene para poder imprimir
factores_ordenados = sorted(factores)

# Para cada animal en el orden original:
for p in factores:
    # -------------------------------------------
    # CÁLCULO DE DEPREDADORES
    # Queremos contar cuántos "x" cumplen:
    #   a <= x - p < b   <=>   p + a <= x < p + b
    #
    # En un arreglo ordenado, esto equivale a contar
    # cuántos valores hay en el intervalo [p+a , p+b)
    #
    # lower_bound(p+b)  = primera posición donde se podría insertar p+b
    # lower_bound(p+a)  = primera posición donde se podría insertar p+a
    #
    # La diferencia entre ambas posiciones es exactamente
    # la cantidad de valores en [p+a, p+b).
    # -------------------------------------------
    dep = bisect.bisect_left(factores_ordenados, p + b) - \
          bisect.bisect_left(factores_ordenados, p + a)
    
    # -------------------------------------------
    # CÁLCULO DE PRESAS
    # Queremos contar cuántos "x" cumplen:
    #   a <= p - x < b   <=>   p - b < x <= p - a
    #
    # Es el intervalo (p - b, p - a]
    #
    # upper_bound(p-a) = índice de primer elemento > (p-a)
    # upper_bound(p-b) = índice de primer elemento > (p-b)
    #
    # upper_bound(p-a) - upper_bound(p-b)
    # nos da cuántos elementos cumplen (p-b, p-a].
    # -------------------------------------------
    pres = bisect.bisect_right(factores_ordenados, p - a) - \
           bisect.bisect_right(factores_ordenados, p - b)

    # Imprimimos la cantidad de depredadores y presas para este animal
    sys.stdout.write(f"{dep} {pres}\n")