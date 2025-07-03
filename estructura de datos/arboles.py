#definimos la clase nodo para representar cada elemento del arbol

class Nodo:
    def __init__(self, valor):
         self.valor=valor
         #referenciamos izquierda
         self.izquierda = None
         #referenciamos derecha
         self.derecha = None
    #definimos funcion para iniciar recorrido
    #de izquierda a derecha              
def recorrido_inorden(nodo):
        if nodo is not None:
            #pasamos por el lado izquierdo
            recorrido_inorden(nodo.izquierda)
            print(nodo.valor)
            recorrido_inorden(nodo.derecha)
            
#creamos lo valores de los nodos
#creamos nodo raiz

raiz = input("ingrese el valor del nodo raiz:")
raiz = Nodo(raiz)

if raiz.valor != None:
    #creamos nodos hijos
    izq = input("ingrese el valor del nodo hijo:")
    raiz.izquierda = Nodo(izq)
    der = input("ingrese el valor del nodo hijo:")
    raiz.derecha = Nodo(der)
    if izq > raiz.valor and der<raiz.valor:
        raiz.izquierda=Nodo(der)
        raiz.derecha=Nodo(izq)
    else:
        if izq < raiz.valor and der>raiz.valor:
            raiz.izquierda=Nodo(izq)
            raiz.derecha=Nodo(der)
if raiz.izquierda != None and raiz.derecha != None:
    #creamos nodos nietos
    izqizq = int(input("ingrese el valor del nodo nieto:"))
    izqder = int(input("ingrese el valor del nodo izquierdo derecho:"))
    derizq = int(input("ingrese el valor del nodo derecho izquierdo:"))
    derder = int(input("ingrese el valor del nodo derecho derecho:"))
    
    if izqizq<int(raiz.valor):
        if izqizq<int(raiz.izquierda.valor):
            raiz.izquierda.izquierda=Nodo(izqizq)
        else:
            raiz.izquierda.derecha=Nodo(izqizq)
    else:
        if izqizq<int(raiz.derecha.valor):
            raiz.derecha.izquierda=Nodo(izqizq)
        else:
            raiz.derecha.derecha=Nodo(izqizq)    
    
    if izqder<int(raiz.valor):
        if izqder<int(raiz.izquierda.valor):
            raiz.izquierda.izquierda=Nodo(izqder)
        else:
            raiz.izquierda.derecha=Nodo(izqder)
    else:
        if izqder<int(raiz.derecha.valor):
            raiz.derecha.izquierda=Nodo(izqder)
        else:
            raiz.derecha.derecha=Nodo(izqder)     
              
    if derizq<int(raiz.valor):
        if derizq<int(raiz.izquierda.valor):
            raiz.izquierda.izquierda=Nodo(derizq)
        else:
            raiz.izquierda.derecha=Nodo(derizq)
    else:
        if derizq<int(raiz.derecha.valor):
            raiz.derecha.izquierda=Nodo(derizq)
        else:
            raiz.derecha.derecha=Nodo(derizq)       
     
    if derder<int(raiz.valor):
        if derder<int(raiz.izquierda.valor):
            raiz.izquierda.izquierda=Nodo(derder)
        else:
            raiz.izquierda.derecha=Nodo(derder)
    else:
        if derder<int(raiz.derecha.valor):
            raiz.derecha.izquierda=Nodo(derder)
        else:
            raiz.derecha.derecha=Nodo(derder)   


#iniciamos recorrido
recorrido_inorden(raiz)
#el resultado es el siguiente:








        