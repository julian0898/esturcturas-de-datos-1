import time

estudiantes ={}
def registrar_estudiante():
 while True:
    print("ingrese la opcion a reaalizar")
    print("1. Registrar estudiante")
    
    opcion=int(input())
    
    if opcion==1:
        print("Registro de Nuevo Estudiante")
        while True:
            id_estudiante = input("Ingrese ID del estudiante: ")
            if id_estudiante in estudiantes:
                print("Error: Ya existe un estudiante con ese ID.")
            else:
                break
        nombre = input("Ingrese nombre del estudiante: ")
        apellido = input("Ingrese apellido del estudiante: ")
        edad = input("Ingrese edad del estudiante: ")
        estudiantes[id_estudiante] = {
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'calificaciones': {}  
        }
        print(f"Estudiante {nombre} {apellido} registrado exitosamente.")
        
        
    if opcion==2:
     print("vuelva pronto")
     break
        
        
inicio =time.time()
registrar_estudiante()
fin = time.time()
tiempo_registro = fin - inicio

print(f"tiempo en recorrer programa: {tiempo_registro:.10f} segundos")