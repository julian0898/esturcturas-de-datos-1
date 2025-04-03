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
