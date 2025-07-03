import time
import random

dicc = {}
tup=()
def estudio_2 ():
    while True:
         print("lista de opciones")
         print("1-llenar un diccionario")
         print("2- llenar una tupla")
         print("3 mostrar diccionario")
         print("4- saber tiempo de ejecucion")
         print("5- mostrar tupla")
         print("6- salir")
         n=int(input("por favor ingrese la opcion a elegir"))
         
         if n==1 :
             objeto=input("ingrese objeto a añadir")
             peso= input("ingresar el peso del objeto")
             color=input("ingrese el color del objeto")
            
             dicc [objeto]={
                 "peso": peso,
                 "color":color,
             }
         elif n==2:
             valores=input("ingrese los valores que estaran en la tupla")
             mi_tupla=tuple(valores.split(","))
         
         elif n==3:
             
              for objeto, informacion in dicc.items():
                  print(f"objetos en el diccionario: {objeto}: peso: {informacion['peso']}, color:{informacion['color']}")    
             
         elif n==4:
             inicio=time.time()
             dicc [objeto]={
                 "peso": peso,
                 "color":color,
             }
             fin=time.time()
             tiempo_ejecucion=fin-inicio
             print(tiempo_ejecucion)
             
         elif n==5:
             print(f"mostrando tupla: {mi_tupla}")
        
        
         elif n==6:
             print("proceso terminado")
             break
                 
                  
inicio=time.time()
estudio_2()
fin=time.time()
tiempo_ejecucion=fin-inicio
print(f"el tiempo tardado es de : {tiempo_ejecucion: 6f}")