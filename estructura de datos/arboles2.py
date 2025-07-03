class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar en el árbol BST
def insertar_en_bst(raiz, valor):
    if valor < raiz.valor:
        if raiz.izquierda is None:
            raiz.izquierda = Nodo(valor)
        else:
            insertar_en_bst(raiz.izquierda, valor)
    elif valor > raiz.valor:
        if raiz.derecha is None:
            raiz.derecha = Nodo(valor)
        else:
            insertar_en_bst(raiz.derecha, valor)
    # Si el valor ya está, no lo insertamos (BST típico no acepta duplicados)

# Recorrido inorden: izquierda - raíz - derecha
def recorrido_inorden(nodo):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda)
        print(nodo.valor)
        recorrido_inorden(nodo.derecha)

# Elegir raíz
raiz_valor = int(input("🔸 Ingresa el valor de la raíz: "))
raiz = Nodo(raiz_valor)

# Ingreso de otros nodos
cantidad = int(input("🔸 ¿Cuántos nodos adicionales querés agregar?: "))
for i in range(cantidad):
    valor = int(input(f"   ➤ Ingrese el valor del nodo #{i+1}: "))
    insertar_en_bst(raiz, valor)

# Mostrar árbol en orden
print("\n✅ Recorrido inorden del BST (valores ordenados):")
recorrido_inorden(raiz)
