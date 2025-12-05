class MergeSort:
    

    def __init__(self):
        self.inv = 0

    def sort(self, lista):
        if len(lista) <= 1:
            return lista
        
        mid = len(lista) // 2
        left = lista[:mid]     # sublista izquierda
        right = lista[mid:]    # sublista derecha

        # Se ordenan recursivamente ambas mitades.
        left = self.sort(left)
        right = self.sort(right)

        l = 0    # índice actual en left
        r = 0    # índice actual en right
        idx = 0  # índice actual en la lista resultado (lista)

        # Mientras haya elementos en ambas mitades por comparar:
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # No hay inversión: el elemento de left va primero.
                lista[idx] = left[l]
                l += 1
            else:

                lista[idx] = right[r]
                r += 1

                # Cantidad de elementos restantes en left:
                # forman inversión con right[r-1].
                self.inv += len(left) - l

            idx += 1

        # Copiar los elementos restantes de left (si quedaron).
        while l < len(left):
            lista[idx] = left[l]
            l += 1
            idx += 1

        # Copiar los elementos restantes de right (si quedaron).
        while r < len(right):
            lista[idx] = right[r]
            r += 1
            idx += 1

        # Lista ya está ordenada y se han contabilizado todas las inversiones.
        return lista
    

n = int(input())
nums = list(map(int, input().split()))

ms = MergeSort()
num_sort = ms.sort(nums)
cant = 0
maxC = -1

for i in range(n):
    act = num_sort[len(num_sort)-1-i]
    cant = 0
    for i in range(len(num_sort)-1-i,-1,-1):
        if act % num_sort[i] == 0:
            cant += 1
            act = num_sort[i]
    maxC = max(maxC,cant)

print(maxC)