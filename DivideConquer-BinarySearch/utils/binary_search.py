def binary_search_min(low, high, check):
    """
    Busca el valor mínimo en el rango [low, high] que cumple la condición 'check'.
    
    Args:
        low (int): Límite inferior.
        high (int): Límite superior.
        check (function): Una función que recibe un entero 'mid' y devuelve
                          True si cumple la condición, False si no.
    Returns:
        int: El valor mínimo que cumple 'check', o None si no se encontró.
    """
    ans = None
    
    while low <= high:
        mid = (low + high) // 2
        
        if check(mid):
            ans = mid        # Guardamos la respuesta válida
            high = mid - 1   # Intentamos buscar un valor más pequeño (a la izquierda)
        else:
            low = mid + 1    # Necesitamos un valor más grande (a la derecha)
            
    return ans