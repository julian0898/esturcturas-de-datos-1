   
print("1- insertar valor a la pila")
print("2-eliminar elemento superior de la pila")
print("3-visualizar contenido de la pila")
n=int(input("ingrese la opcion a elegir")) 
pila=[1,2]    
    
if n==1:
    elemento=input("escriba el elemento que desea ingresar")
    pila.append(elemento)
    print("el elemento se ha insertado correctamente")
    print("la pila es: ",pila)
elif n==2:
    if len(pila)==0:
        print("la pila esta vacia")
    else:
        elemento=pila.pop()
        print("el elemento eliminado es: ",elemento)
        print("la pila es: ",pila)
elif n==3:
    if len(pila)==0:
        print("la pila esta vacia")
    else:
        print("la pila es: ",pila)
else:
    print("opcion no valida")

        
       
        
        

    