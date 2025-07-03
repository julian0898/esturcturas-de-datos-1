class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = padre  # Nuevo: referencia al padre

# Función para insertar en el BST y asignar padre
def insertar_en_bst(raiz, valor):
    if valor < raiz.valor:
        if raiz.izquierda is None:
            raiz.izquierda = Nodo(valor, raiz)
        else:
            insertar_en_bst(raiz.izquierda, valor)
    elif valor > raiz.valor:
        if raiz.derecha is None:
            raiz.derecha = Nodo(valor, raiz)
        else:
            insertar_en_bst(raiz.derecha, valor)

# Recorrido inorden con info del padre
def recorrido_inorden(nodo):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda)
        padre_valor = nodo.padre.valor if nodo.padre else "None"
        print(f"Valor: {nodo.valor}, Padre: {padre_valor}")
        recorrido_inorden(nodo.derecha)

# Elegir raíz
raiz_valor = int(input("🔸 Ingresa el valor de la raíz: "))
raiz = Nodo(raiz_valor)

# Ingreso de otros nodos
cantidad = int(input("🔸 ¿Cuántos nodos adicionales querés agregar?: "))
for i in range(cantidad):
    valor = int(input(f"   ➤ Ingrese el valor del nodo #{i+1}: "))
    insertar_en_bst(raiz, valor)

# Mostrar árbol en orden con padres
print("\n✅ Recorrido inorden del BST (con padres):")
recorrido_inorden(raiz)

