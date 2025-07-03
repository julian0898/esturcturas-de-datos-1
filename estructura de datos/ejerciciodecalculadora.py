#escribe un programa en python que solicite al usuario los siguientes datos 
# su nombre tipo string 
# su edad tipo int
# total de la cuenta float
# porcentaje que desea de dejar de propina tipo int
# el programa debe asegurarse que los valores ingresados sean validos debe calcular la cantidad de propina
# el total a pagar cuenta mas propina y un mensaje personalizado segun la edad del usuario.
#brindele al usuario la posibilidad de elejir productos de un menu antes de calcular la propina

#informacion del usuario
nombre=str(input("ingrese su nombre: "))
edad=int(input("ingrese su edad: "))

#menu de productos

productos=[
             ("menu del dia",10000),
             ("almuerzo ejecutivo",15000),
             ("plato a la carta",12000),
             ("bebida",3000),
             ("postre",5000)
     ]

#menu de opciones
for i, (producto,precio) in enumerate(productos,1):
    print(f"{i}. {producto} - ${precio}")
    
compra=True
total_compra=[]
while compra:
    opcion=int(input("por favor seleccione un productos: (si desea salir presiones 0)"))
    
    if opcion==0:
        compra=False
        
    elif 1<=opcion<=len(productos):
        producto,precio=productos[opcion-1]
        print(f"{producto} ha sido ordenado")
        total_compra.append((producto,precio))
        
    else:
        print("opcion invalida")
        
#calcular total de la compra        
    
total=sum(precio for _, precio in total_compra)
print(f"el total de la compra es : ${total}")

#calcular propina
propina=int(input("ingrese el porcentaje de propina que desea dejar: "))
total_propina=total*propina/100
print(f"la propina es de : ${total_propina}")

#total a pagar
total_pagar=total+total_propina 
print(f"el total a pagar es de : ${total_pagar}")


if edad<18:
    print("eres menor de edad")
elif 18<=edad<65:
    print("eres mayor de edad")
else:
    print("eres adulto mayor")