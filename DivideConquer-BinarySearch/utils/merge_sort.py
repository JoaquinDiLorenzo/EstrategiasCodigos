class MergeSort:
    """
    Implementa merge sort para:
    - Ordenar una lista de números.
    - Contar la cantidad de inversiones del arreglo original.

    Definición:
        Una inversión es un par (i, j) tal que:
            - i < j
            - lista[i] > lista[j]

    Uso típico (problema "contar inversiones"):
        ms = MergeSort()
        ms.sort(a)          # ordena 'a' in-place
        print(ms.inv)       # cantidad total de inversiones

    Complejidad:
        Tiempo:  O(n log n)
        Memoria: O(n) (por las listas temporales left/right)
    """

    def __init__(self):
        # Contador de inversiones acumulado durante el proceso de merge sort.
        self.inv = 0

    def sort(self, lista):
        """
        Ordena la lista usando merge sort y, en el proceso,
        actualiza self.inv con la cantidad de inversiones.

        Parámetros:
            lista (list[int | float]): lista de valores comparables.

        Retorna:
            list: la misma lista, pero ordenada (también modificada in-place).
        """

        # Caso base: lista vacía o de un solo elemento ya está ordenada.
        if len(lista) <= 1:
            return lista
        
        # 1) DIVIDIR: se parte la lista en dos mitades.
        mid = len(lista) // 2
        left = lista[:mid]     # sublista izquierda
        right = lista[mid:]    # sublista derecha

        # Se ordenan recursivamente ambas mitades.
        left = self.sort(left)
        right = self.sort(right)

        # 2) COMBINAR (MERGE): se mezclarán 'left' y 'right' en 'lista',
        # manteniendo el orden y contando inversiones.

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
                # Hay inversiones:
                #    left[l] > right[r]
                # Como 'left' y 'right' están ordenadas,
                # todos los elementos desde left[l] hasta left[-1]
                # son mayores que right[r].
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
