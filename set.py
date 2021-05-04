#set es una colección:
#sin orden, sin indices, sin repetidos
#no se pueden modificar los elementos
#se puede agregar nuevos y eliminar

planetas = {"Marte","Júpiter","Venus"}
#agregar .add
planetas.add("Marte") #No lo agrega porque ya pertenece
planetas.add("Neptuno")
print(planetas)
print("Marte" in planetas)

#eliminar
#Si no existe, da error
planetas.remove("Neptuno")
print(planetas)
#Si se usa discard no arroja error
planetas.discard("Neptuno")
#clear elimina todo lo que está adentro del conjunto
planetas.clear()
print(planetas)
del planetas
print(planetas)