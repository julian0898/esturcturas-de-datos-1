# analizamos la complejidad comparando busqueda lineal con busqueda binaria
import time # permite medir el tiempo de ejecucio
import random # genera numeros aleatorios

def busqueda_lineal(arr, objetivo):
    for i, num in enumerate(arr):
        if num == objetivo:
            return i
    return -1 # el valor no fue encontrado

# definimos la busqueda binaria
def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1 # no se encontro elemento

# generar datos para la prueba
n = 10**6 # Tl 1 millon
datos = sorted(random.sample(range(n*10), n)) # lista para busqueda ordenada
objetivo = random.choice(datos) # elegimos un valor al azar de la lista

# medicion de tiempo lineal
inicio = time.time() # inicia el cronometro
busqueda_lineal(datos, objetivo)
fin = time.time() # finaliza el cronometro
tiempo_lineal = fin - inicio # calcular tiempo

# medicion tiempo busqueda binaria
inicio = time.time() # inicia el cronometro
busqueda_binaria(datos, objetivo)
fin = time.time() # finaliza el cronometro
tiempo_binario = fin - inicio # calcular tiempo

# imprimir resultados
print(f"busqueda lineal (O(n)): {tiempo_lineal:.6f} segundos")
print(f"busqueda binaria (O(log n)): {tiempo_binario:.6f} segundos")





