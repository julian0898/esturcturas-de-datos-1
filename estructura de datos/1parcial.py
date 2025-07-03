

import time
import random

def producs():
    producto = []  
    while True:
        print("lista de opciones")
        print("1- cuantos productos desea ingresar")
        print("2- mostrar productos ingresados")
        print("3- productos con un precio mayor a 10.000")
        print("4- salir")
        n = int(input("por favor ingrese la opcion a elegir"))
        if n == 1:
            cantidad_productos = float(input("ingrese la cantidad de productos que desea ingresar"))
            for i in range(int(cantidad_productos)):
                nombre_del_producto = input("ingrese el nombre del producto")
                precio_unitario = float(input("ingrese el precio unitario del producto"))
                mytupla = (nombre_del_producto, int(precio_unitario))
                producto.append(mytupla)
        elif n == 2:
            print(f"productos ingresados: {producto}")
        elif n == 3:
            cont = 0
            for i in producto:
                if i[1] > 10000:
                    cont += 1
            print(f"productos con precio mayor a 10.000: {cont}")
        elif n == 4:
            print("!vuelva pronto")
            break

inicio = time.time()
producs()
fin = time.time()
tiempo = fin - inicio
print(f"el tiempo tardado: {tiempo: .6f} segundos")