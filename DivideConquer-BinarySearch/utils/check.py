def es_posible(medio, k, array):
    suma = 0
    cant_sub = 1

    for x in array:
        if suma + x > medio:
            cant_sub += 1
            suma = 0
        suma += x
    return cant_sub <= k