#investigar e implementar una pila usando vectores en python e indique cual es la sintaxis basica

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print("Pila:", stack)
print("Extraer un elemento:", stack.pop())
print("Pila actualizada:", stack)
print("Extraer un elemento:", stack.pop())
print("Pila actualizada:", stack)


#implementar pila llena
stack = [1, 2, 3, 4, 5] 
print("Pila:", stack)
stack.append(6)
print("Pila actualizada:", stack)
stack.append(7)
print("Pila actualizada:", stack)

#dada la palabra ingenieria almacenada dentro de una pila, presento como resultado la misma palabra invertida
pila=[]
pila.append('i')
pila.append('n')
pila.append('g')
pila.append('e')
pila.append('n')
pila.append('i')
pila.append('e')
pila.append('r')
pila.append('i')
pila.append('a')
print("pila normal: ",pila)
pila.reverse()
print("pila invertida: ",pila)

for i in range(len(pila)):
    print(pila.pop())
    
#que se ingrese cualquier palabra y se invierta
palabra = input("Ingrese una palabra: ")
pila = list(palabra)

print("Pila normal: ", pila)
pila.reverse()
print("Pila invertida: ", pila)

for i in range(len(pila)):
    print(pila.pop(), end='')





    


    
    
   