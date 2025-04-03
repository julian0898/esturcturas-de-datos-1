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
