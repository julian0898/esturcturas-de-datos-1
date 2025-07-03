def es_reflexiva(relacion, conjunto):
    """Verifica si la relación es reflexiva."""
    for a in conjunto:
        if (a, a) not in relacion:
            return False
    return True

def es_simetrica(relacion):
    """Verifica si la relación es simétrica."""
    for (a, b) in relacion:
        if (b, a) not in relacion:
            return False
    return True

def es_transitiva(relacion):
    """Verifica si la relación es transitiva."""
    for (a, b) in relacion:
        for (c, d) in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True

def es_antisimetrica(relacion):
    """Verifica si la relación es antisimétrica."""
    for (a, b) in relacion:
        if (b, a) in relacion and a != b:
            return False
    return True

def verificar_relacion(relacion, conjunto):
    """Verifica todas las propiedades de la relación."""
    print("Reflexiva:", es_reflexiva(relacion, conjunto))
    print("Simétrica:", es_simetrica(relacion))
    print("Transitiva:", es_transitiva(relacion))
    print("Antisimétrica:", es_antisimetrica(relacion))
    if es_reflexiva(relacion, conjunto)==True and es_simetrica(relacion)==True and es_transitiva(relacion)==True:
        print("La relación R es equivalente")
    else:
        print("La relación R NO es equivalente")
    if es_reflexiva(relacion, conjunto)==True and es_antisimetrica(relacion)==True and es_transitiva(relacion)==True:
        print("La relación R es de orden")
    else:
        print("La relación R NO es de orden")
# Ejemplo de uso
conjunto = set(input("Ingrese los elementos del conjunto separados por comas: ").split(','))
relacion = set(tuple(a.strip('()').split(',')) for a in input("Ingrese las relaciones en formato (A,B) separadas por espacio: ").split())
verificar_relacion(relacion,conjunto)