def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    """
    Implementación de búsqueda binaria utilizando recursión.
    Divide el problema en mitades hasta encontrar el elemento.
    """
    # Caso base: El elemento no está en la lista
    if izquierda > derecha:
        return -1

    # Calcular el punto medio
    medio = (izquierda + derecha) // 2

    # Caso base: El elemento está en el medio
    if lista[medio] == objetivo:
        return medio

    # Llamada recursiva: Buscar en la mitad izquierda
    elif lista[medio] > objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)

    # Llamada recursiva: Buscar en la mitad derecha
    else:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)

# Bloque de ejecución principal
if __name__ == "__main__":
    datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    buscado = 23
    
    print(f"Lista ordenada: {datos}")
    resultado = busqueda_binaria_recursiva(datos, buscado, 0, len(datos) - 1)

    if resultado != -1:
        print(f"¡Éxito! El número {buscado} se encuentra en el índice {resultado}.")
    else:
        print(f"El número {buscado} no existe en la lista.")
