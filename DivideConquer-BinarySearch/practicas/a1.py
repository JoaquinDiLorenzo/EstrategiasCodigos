import sys 

class MergeSort:
    def __init__(self):
        self.inv = 0  # contador de inversiones

    def sort(self, lista):
        # caso base: lista de tamaño 0 o 1 ya está ordenada
        if len(lista) <= 1:
            return lista
        
        # dividir
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        left = self.sort(left)
        right = self.sort(right)

        # combinar contando inversiones
        l = 0  # índice en left
        r = 0  # índice en right
        idx = 0  # índice en lista (resultado)

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                lista[idx] = left[l]
                l += 1
            else:
                lista[idx] = right[r]
                r += 1
                # todos los elementos restantes en left (desde l hasta el final)
                # son mayores que right[r-1], entonces suman inversiones
                self.inv += len(left) - l
            idx += 1

        # copiar restos de left y right
        while l < len(left):
            lista[idx] = left[l]
            l += 1
            idx += 1

        while r < len(right):
            lista[idx] = right[r]
            r += 1
            idx += 1

        return lista

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().strip().split()))

array = array[:n]

ms = MergeSort()
ms.sort(array)
sys.stdout.write(f"{ms.inv}")