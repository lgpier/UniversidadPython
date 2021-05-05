class Persona:
    def __init__(self, nombre, edad, *valores, **diccionario):
        self.nombre = nombre
        self.edad = edad
        self.valores = valores
        self.diccionario = diccionario
        
    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Valores(tupla): ", self.valores)
        print("Diccionario: ", self.diccionario)

p1 = Persona("Lucas", 28)
p1.desplegar()
print("")
p2 = Persona("Dafne", 27, 2,4,5)
p2.desplegar()
print("")
p3=Persona("Alma",9, 4,9, m="Manzana", p="Pera" , j="Jamaica")
p3.desplegar()
