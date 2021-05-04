class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#modificar valores

Persona.nombre = "Lucas"
Persona.edad = 28

#acceder a valores
print(Persona.edad)
print(Persona.nombre)
print("")

"""Esto de asignar atributos a las clases no se hace,
lo que se hace es crear objetos(instancias) de esa clase"""


#crear un objeto
persona = Persona("Dafne","27")
print(persona.nombre)
print(persona.edad)
print(id(persona))
print("")

persona2 = Persona("Alma", "9")
print(persona2.edad)
print(persona2.nombre)
print(id(persona2))
