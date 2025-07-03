"""""
#el usuario debe registrar informacion personal (nombre,apellido,edad,saldo de la cuenta) se almacenara una lista de productos disponibles en la tienda cada uno con su precio, 3 se permitira que el usuario agregue productos a su carrito de compras , 4 se calculara el total de la compra y se verificara si el saldo del usuario es suficiente, 5 se mostrara un rasumen con los productos comprados y el saldo restante.
"""

#ingreso de datos
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=int(input("ingrese su edad: "))#int
saldo=float(input("ingrese su saldo: "))#float

#lista de productos
productos=[
           ("portatil",1200000),
           ("mouse",45000),
           ("teclado",60000),
           ("monitor",80000),
           ("audifonos",50000),
           
           ]

print("\nproductos disponibles:")
for i, (producto,precio) in enumerate(productos,1):
    print(f"{i}. {producto} - ${precio}")
    
#carrito de compras
carrito=[]
comprando=True
while comprando:
    opcion=int(input("seleccione un producto: (0 para salir) "))
    if opcion==0:
        comprando=False
    elif 1<=opcion<=len(productos):
        producto, precio=productos[opcion-1]
        carrito.append((producto,precio))
        print(f"{producto} ha sido agregado al carrito")
    else:
        print("opcion invalida")
        
     #calcular total de la compra
total_compra=sum(precio for _, precio in carrito)
print(f"el total de la compra es : ${total_compra}")
        
#verificar si al usuario le alcanza 
if saldo>=total_compra:
    saldo-=total_compra
    print(f"compra exitosa, su saldo es de ${saldo}")
    
else:
    print(f"saldo insuficiente ${saldo}")
            
        
           
    
    
