def busqueda_secuencial(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

# Ejemplo de uso
lista = [3, 5, 2, 4, 9]
objetivo = 4
resultado = busqueda_secuencial(lista, objetivo)

if resultado != -1:
    print(f'Elemento encontrado en el índice: {resultado}')
else:
    print('Elemento no encontrado')