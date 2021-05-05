class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)
    
        
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)


p1 = Persona("Lucas",28)
print(p1)

empleado = Empleado("Dafne",27,70000.00)
print(empleado)

empleado.nombre = "Dafne Noemi"
empleado.sueldo = 75000.00
print(empleado)
