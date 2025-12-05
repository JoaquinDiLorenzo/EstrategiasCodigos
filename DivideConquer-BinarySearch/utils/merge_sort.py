class MergeSort:
    """
    MERGE SORT GENÉRICO + CONTADOR DE INVERSIONES

    ¿Qué hace esta plantilla?
    - Ordena un array en O(n log n).
    - Cuenta la cantidad de inversiones (pares i<j con a[i] > a[j]).
    - Te deja un lugar clarísimo para agregar lógica extra de
      Divide & Conquer basada en "comparar mitad izquierda vs derecha".

    USO TÍPICO 1: solo ordenar
        ms = MergeSort()
        ms.sort(a)
        # ahora 'a' está ordenada

    USO TÍPICO 2: contar inversiones
        ms = MergeSort()
        ms.sort(a)
        print(ms.inv)   # cantidad total de inversiones en el array original

    USO TÍPICO 3: adaptar a otros problemas
        - Editar la sección marcada como "ZONA CUSTOM" dentro de _merge()
          para acumular la info que pida el enunciado.
    """

    def __init__(self):
        # Contador de inversiones (podés agregar más acumuladores si querés).
        self.inv = 0

    # -------------------------------------------------------
    # INTERFAZ PÚBLICA
    # -------------------------------------------------------
    def sort(self, arr):
        """
        Ordena 'arr' IN-PLACE usando merge sort.
        Devuelve la misma referencia para conveniencia.

        arr: lista de números (o cualquier cosa comparable con <=).
        """
        n = len(arr)
        if n <= 1:
            return arr

        # buffer auxiliar para hacer el merge sin crear listas nuevas todo el tiempo
        temp = [None] * n
        self._sort(arr, temp, 0, n - 1)
        return arr

    # -------------------------------------------------------
    # PARTE RECURSIVA (DIVIDE)
    # -------------------------------------------------------
    def _sort(self, arr, temp, left, right):
        """
        Ordena arr[left..right] y actualiza contadores (inversiones, etc.).
        """
        if left >= right:
            return

        mid = (left + right) // 2

        # ordenar mitad izquierda y mitad derecha
        self._sort(arr, temp, left, mid)
        self._sort(arr, temp, mid + 1, right)

        # combinar ambas mitades
        self._merge(arr, temp, left, mid, right)

    # -------------------------------------------------------
    # PARTE DE COMBINAR (MERGE) + ZONA CUSTOM
    # -------------------------------------------------------
    def _merge(self, arr, temp, left, mid, right):
        """
        Mezcla arr[left..mid] y arr[mid+1..right] (ya ordenados)
        en 'temp', luego copia el resultado a 'arr'.

        Acá es donde:
          - se cuentan las INVERSIONES,
          - y donde podés agregar lógica extra para otros problemas.
        """

        i = left      # puntero en mitad izquierda
        j = mid + 1   # puntero en mitad derecha
        k = left      # puntero en temp
        inv_count = 0 # contador local de inversiones

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                # Caso "normal": el elemento de la izquierda va primero.
                temp[k] = arr[i]
                i += 1
            else:
                # Caso "cruzado": arr[i] > arr[j]
                temp[k] = arr[j]

                # ==========================
                # ZONA CUSTOM (INVERSIONES)
                # ==========================
                # Como las mitades están ordenadas, si arr[i] > arr[j],
                # entonces TODOS arr[i], arr[i+1], ..., arr[mid]
                # son > arr[j]. Eso forma (mid - i + 1) inversiones.
                inv_count += (mid - i + 1)
                # Si el problema pidiera otra cosa (por ejemplo,
                # contar pares con cierta propiedad), este es el
                # lugar típico donde se acumulan esas cosas.
                # ==========================

                j += 1

            k += 1

        # Copiar lo que queda en la izquierda
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        # Copiar lo que queda en la derecha
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        # Copiar resultado ordenado de temp a arr
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]

        # Actualizar contador global de inversiones
        self.inv += inv_count