class Persona:
    def __init__(self, nombre):
        #Se colocan los __ para encapsular
        self.__nombre = nombre
    
    #Obtener
    def getNombre(self):
        return self.__nombre
    #definir
    def setNombre(self,nombre):
        self.__nombre = nombre
        

p1 = Persona("Lucas")
print(p1.getNombre())

p1.setNombre("Dafne")
print(p1.getNombre())
