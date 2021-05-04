#está compuesto por llave,valor (key,value)

diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Objet Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)
#largo
print(len(diccionario))
#accediendo a un elemento
print(diccionario["IDE"])
print(diccionario.get("IDE"))
#modificando valores
diccionario["IDE"] = "Integrated Development EnvironmenT"
print(diccionario["IDE"])
#iterar
for termino in diccionario:
    print(termino)
print("")
for termino in diccionario:
    print(diccionario[termino])
print("")
for valor in diccionario.values():
    print(valor)
print("")
#comprobar existencia de elemento
print("IDE" in diccionario)
print("IDe" in diccionario)
print("")
#agregar nuevos valores
diccionario["PK"] = "Primary Key"
print(diccionario)
#remover elementos
diccionario.pop("IDE")
print(diccionario)

    