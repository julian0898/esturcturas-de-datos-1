#crre un programa en python de gestion de estudiantes que permita al usuario registrar estudiantes y sus notas, el programa debe permitir al usuario ver el listado de estudiantes y sus notas, calcular el promedio de notas de un estudiante en particular y el promedio general de todos los estudiantes, el programa debe tener un menu de opciones que permita al usuario seleccionar que accion desea realizar.

#diccionario para almacenar informacion de los estudaintes con su nombre id y notas
#sets para almacenar materias sin duplicarlas
#listas y tuplas para organizar los datos de cada estudiante
#while para mantener el programa en ejecucion

#definir las variables
# Inicialización de estructuras de datos
estudiantes = {}  # Diccionario para almacenar información de estudiantes: {id: {info}}
materias = set()  # Conjunto para almacenar materias sin duplicados

while True:
    print("\nSISTEMA DE REGISTRO DE ESTUDIANTES")
    print("1- Registrar nuevo estudiante")
    print("2- Asignar calificaciones")
    print("3- Mostrar promedio de un estudiante")
    print("4- Mostrar estudiantes aprobados y reprobados")
    print("5- Consultar estudiantes y materias registradas")
    print("6- Salir")
    opcion = input("\nSeleccione una opción: ")

    # Opción 1: Registrar nuevo estudiante
    if opcion == "1":
        print("\nRegistro de Nuevo Estudiante")
        
        while True:
            id_estudiante = input("Ingrese ID del estudiante: ")
            if id_estudiante in estudiantes:
                print("Error: Ya existe un estudiante con ese ID.")
            else:
                break
        
        nombre = input("Ingrese nombre del estudiante: ")
        apellido = input("Ingrese apellido del estudiante: ")
        edad = input("Ingrese edad del estudiante: ")
        
        # Crear diccionario con información básica del estudiante
        estudiantes[id_estudiante] = {
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'calificaciones': {}  # Diccionario para almacenar calificaciones: {materia: nota}
        }
        
        print(f"Estudiante {nombre} {apellido} registrado exitosamente.")

    # Opción 2: Asignar calificaciones
    elif opcion == "2":
        print("\nAsignación de Calificaciones")
        
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            id_estudiante = input("Ingrese ID del estudiante: ")
            if id_estudiante not in estudiantes:
                print("Estudiante no encontrado.")
            else:
                materia = input("Ingrese nombre de la materia: ")
                materias.add(materia)  # Agregar materia al conjunto
                
                while True:
                    try:
                        calificacion = float(input("Ingrese calificación (0-5): "))
                        if 0 <= calificacion <= 5:
                            break
                        else:
                            print("La calificación debe estar entre 0 y 5.")
                    except ValueError:
                        print("Por favor, ingrese un valor numérico válido.")
                
                # Asignar calificación
                estudiantes[id_estudiante]['calificaciones'][materia] = calificacion
                print(f"Calificación asignada correctamente a {estudiantes[id_estudiante]['nombre']}.")

    # Opción 3: Mostrar promedio de un estudiante
    elif opcion == "3":
        print("\n--- Promedio de Calificaciones ---")
        
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            id_estudiante = input("Ingrese ID del estudiante: ")
            if id_estudiante not in estudiantes:
                print("Estudiante no encontrado.")
            else:
                estudiante = estudiantes[id_estudiante]
                calificaciones = estudiante['calificaciones']
                
                # Cálculo de promedio
                if not calificaciones:
                    promedio = 0
                else:
                    promedio = sum(calificaciones.values()) / len(calificaciones)
                
                print(f"Estudiante: {estudiante['nombre']} {estudiante['apellido']}")
                print(f"Promedio: {promedio:.2f}")
                
                if promedio >= 3.0:
                    print("Estado: APROBADO")
                else:
                    print("Estado: REPROBADO")

    # Opción 4: Mostrar estudiantes aprobados y reprobados
    elif opcion == "4":
        print("\nLista de Estudiantes Aprobados y Reprobados")
        
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            aprobados = []
            reprobados = []
            
            for id_est, info in estudiantes.items():
                calificaciones = info['calificaciones']
                
                # Cálculo de promedio
                if not calificaciones:
                    promedio = 0
                else:
                    promedio = sum(calificaciones.values()) / len(calificaciones)
                
                nombre_completo = f"{info['nombre']} {info['apellido']}"
                
                # Crear tupla con información del estudiante
                datos_estudiante = (id_est, nombre_completo, promedio)
                
                if promedio >= 3.0:
                    aprobados.append(datos_estudiante)
                else:
                    reprobados.append(datos_estudiante)
            
            print("\nESTUDIANTES APROBADOS:")
            if aprobados:
                for est in aprobados:
                    print(f"ID: {est[0]} - Nombre: {est[1]} - Promedio: {est[2]:.2f}")
            else:
                print("No hay estudiantes aprobados.")
            
            print("\nESTUDIANTES REPROBADOS:")
            if reprobados:
                for est in reprobados:
                    print(f"ID: {est[0]} | Nombre: {est[1]} | Promedio: {est[2]:.2f}")
            else:
                print("No hay estudiantes reprobados.")

    # Opción 5: Consultar estudiantes y materias registradas
    elif opcion == "5":
        print("\n Consulta de Registros ")
        
        while True:
            print("\nOpciones de consulta:")
            print("1. Ver lista de estudiantes")
            print("2. Ver lista de materias")
            print("3. Ver detalles de un estudiante")
            print("4. Volver al menú principal")
            
            opcion_consulta = input("\nSeleccione una opción: ")
            
            if opcion_consulta == "1":
                print("\nLISTA DE ESTUDIANTES:")
                if estudiantes:
                    for id_est, info in estudiantes.items():
                        print(f"ID: {id_est} | Nombre: {info['nombre']} {info['apellido']}")
                else:
                    print("No hay estudiantes registrados.")
                    
            elif opcion_consulta == "2":
                print("\nLISTA DE MATERIAS:")
                if materias:
                    for materia in materias:
                        print(f"- {materia}")
                else:
                    print("No hay materias registradas.")
                    
            elif opcion_consulta == "3":
                id_estudiante = input("Ingrese ID del estudiante: ")
                if id_estudiante in estudiantes:
                    est = estudiantes[id_estudiante]
                    print(f"\nID: {id_estudiante}")
                    print(f"Nombre: {est['nombre']} {est['apellido']}")
                    print(f"Edad: {est['edad']}")
                    print("\nCalificaciones:")
                    
                    if est['calificaciones']:
                        for materia, nota in est['calificaciones'].items():
                            print(f"- {materia}: {nota}")
                    else:
                        print("No tiene calificaciones registradas.")
                        
                    # Cálculo de promedio
                    calificaciones = est['calificaciones']
                    if not calificaciones:
                        promedio = 0
                    else:
                        promedio = sum(calificaciones.values()) / len(calificaciones)
                    
                    print(f"\nPromedio: {promedio:.2f}")
                    print(f"Estado: {'APROBADO' if promedio >= 3.0 else 'REPROBADO'}")
                else:
                    print("Estudiante no encontrado.")
                    
            elif opcion_consulta == "4":
                break
                
            else:
                print("Opción no válida. Intente nuevamente.")

    # Opción 6: Salir
    elif opcion == "6":
        print("¡vuelva pronto!")
        break

    # Opción inválida
    else:
        print("Opción no válida. Intente nuevamente.")

            
        
            
            
            
      