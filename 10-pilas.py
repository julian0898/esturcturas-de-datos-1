#1investigar que son los terminos notacion infija,notacion posfija y notacion prefija,brinde dos ejemplos de cada uno y explique como se hace evaluacion de expreciones posfijas 
#2como convertir una expresion infija a posfija
#3 resuelva lo siguiente en python: cree un programa que verifique si una expresion matematica contiene los simbolos de apretura y cierre correctamente balanceados. se deben validar parentesis, corchetes y llaves.
#requisitos: usar una pila para almacenar los simbolos de apertura
# cada simbolo de cierre debe coincidir co el tipo de apertura reciente 
# la expresion debe ser ecorrida caracter por caracter

pila = []
expresion = input("Ingrese la expresión a validar: ")

for i in expresion:
    if i == "(" or i == "[" or i == "{":
        pila.append(i)
    elif i == ")" or i == "]" or i == "}":
        if len(pila) > 0:
            simbolo = pila.pop()
            if simbolo == "(":
                if i != ")":
                    print("La expresión no es válida")
                    break
            elif simbolo == "[":
                if i != "]":
                    print("La expresión no es válida")
                    break
            elif simbolo == "{":
                if i != "}":
                    print("La expresión no es válida")
                    break
        else:
            print("La expresión no es válida")
            break
else:
    if len(pila) == 0:
        print("La expresión es válida")
    else:
        print("La expresión no es válida")







