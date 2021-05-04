"""Crear clase rectangulo, atributos de base y altura
definirlos en init, crear metodo calculararea(), debe
calcular el area a partir de la base y la altura ya dada.
Luego tenemos que probarlo solicitando el valor de 
base y altura a un usuario."""

#creando clase
class Rectangulo:
    
    #definiendo los atributos de la clase (constructor)
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    #creando un metodo de la clase
    def calculararea(self):
        return self.base * self.altura

base = int(input("Ingrese el valor de la base: "))
while base <= 0:
    print("Debe ingresar un valor positivo")
    base = int(input("Ingrese el valor de la base: "))

altura = int(input("Ingrese el valor de la altura: "))
while altura <= 0:
    print("Debe ingresar un valor positivo")
    altura = int(input("Ingrese el valor de la altura: "))

#creando objeto de la clase
rectangulo = Rectangulo(base,altura)
print(rectangulo.calculararea())

rectangulo1 = Rectangulo(2,4)
print(rectangulo1.calculararea())