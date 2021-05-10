class Miclase:
    
    variableClase = "Variable de Clase"
    
    def __init__(self,variableInstancia):
        self.variableInstancia = "Variable de Instancia"

print(Miclase.variableClase)
objeto1 = Miclase("Variable Instancia")
#Solo asociado a la clase
Miclase.variableInstancia = "Modificando variable de instancia" 
print(Miclase.variableInstancia) #Valor distinto al de abajo
print(objeto1.variableInstancia) #Valor distinto al de arriba

#Se puede acceder a las variables de clase desde los objetos
print(objeto1.variableClase)
#Podemos acceder a las variables de clases con el nombre de la clase
print(Miclase.variableClase)

#Esta modificación se asocia únicamente con el objeto que la modifica
objeto1.variableClase = "Modificando variable de clase"
print(objeto1.variableClase)
print(Miclase.variableClase)
objeto2 = Miclase("Nuevo valor de variable de instancia")
print(objeto2.variableClase)

objeto3 = Miclase("Tercer objeto")

#Si modifico desde la clase, todos los objetos sufren las modificaciones. Exceptuando los objetos que hayan modificado el valor. Como es el caso de objeto1
Miclase.variableClase ="Cambio desde la clase"
print(objeto1.variableClase)
print(objeto2.variableClase)
print(objeto3.variableClase)