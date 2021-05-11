class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    #Metodo sobreeescrito de la clase padre Object
    def __add__(self, otro):
        return self.__nombre +" "+ otro.__nombre 
         
    def __sub__(self,otro):
        return "Operación no soportada"
        
p1 = Persona("Juan")
p2 = Persona("Karla")

#Sobrecarga es agregar una nueva funcionalidad, en este caso a +
print(p1 + p2)
print(p1 - p2)