#diccionarios python

carros ={
    "mazda":2005,
    "toyota":2007,
    "renault":2006,
}
print(carros)
print(carros.get("mazda"))

#cambiar elemento
carros["toyota"]=2015
print(carros)

print("keys")
#mostrar elemntos key
for x in carros:
    print(x)
    
#mostrar elementos value
print("valores")
for x in carros:
    print(carros[x])
  
print("mostrando elemnto y valor")
  
#mostrar elementos key y value
for x,y in carros.items():
    print(x,y)
    