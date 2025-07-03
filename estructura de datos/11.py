#definicion de cola y su estructura principal
#cuales son las operaciones basicas de una cola
#como se pueden hacer la siguientes operaciones en python:
#a. crear cola, b. borrar cola, c. verificar si la cola esta vacia, d. verificar si la cola esta llena, e.QUEVE, f. DEQUEVE, g. verificar tamaño
#elabore un algoritmo que permita implementar una cola con listas enlazadas
#explique como se puede implementar una cola con vectores
#elabore un algoritmo de una cola con vectores
#cuales son las principales aplicaciones de las colas


cola = None  

cola = [10, None] 
cola[1] = [20, None] 
cola[1][1] = [30, None]  


nodo = cola
while nodo is not None:
    print(nodo[0], end=" -> " if nodo[1] else "\n")
    nodo = nodo[1]

# Desencolar 
valor = cola[0]  
cola = cola[1]  

print("Desencolado:", valor)

# Mostrar la cola después de desencolar
nodo = cola
while nodo is not None:
    print(nodo[0], end=" -> " if nodo[1] else "\n")
    nodo = nodo[1]



#cola con vectores

cola = []


cola.append(10)  
cola.append(20)  
cola.append(30)  

print("Cola después de encolar:", cola)


if cola:  
    valor = cola.pop(0)
    print("Desencolado:", valor)
else:
    print("Cola vacía, no se puede desencolar.")


print("Cola después de desencolar:", cola)
