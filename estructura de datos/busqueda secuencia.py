import time

def busqueda(lista, valor, memoria={}):
    print(f"Lista: {lista}")
    
    if lista[0] == valor:
        print(f"Encontrado al inicio")
        return 0
    
    if lista[-1] == valor:
        print(f"Encontrado al final")
        return len(lista) - 1
    
    if valor in memoria and memoria[valor] < len(lista) and lista[memoria[valor]] == valor:
        print(f"Encontrado usando memoria")
        return memoria[valor]
    
    for i in range(1, len(lista) - 1):
        if lista[i] == valor:   
            memoria[valor] = i  
            print(f"Encontrado en posición {i}")
            return i
    
    print("No encontrado")
    return -1


numeros = [15, 7, 23, 4, 9, 31, 44, 8, 16]
historial = {}
print("Lista de números:", numeros)

while True:
    entrada = input("\nNúmero a buscar (o 'salir'): ")
    if entrada.lower() == 'salir': break
    
    try:
        valor = int(entrada)
        inicio = time.time()
        busqueda(numeros, valor, historial)
        fin = time.time()
        tiempo = fin - inicio
        print(f"El tiempo tardado: {tiempo:.6f} segundos")
    except ValueError:
        print("Ingrese un número válido")
        
        
        19              