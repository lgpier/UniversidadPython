"""Crear clase caja, atributos alto, ancho y largo. Metodo para calcular volumen. Largo*Ancho*Alto. Solicitar al usuario que ingrese datos"""

#creando clase
class Caja:
    
    #definiendo los atributos de la clase (constructor)
    def __init__(self,largo,ancho,alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        
    #creando un metodo de la clase
    def calcularVolumen(self):
        return self.largo * self.alto * self.ancho

largo = int(input("Ingrese el valor de la base: "))
while largo <= 0:
    print("Debe ingresar un valor positivo")
    largo = int(input("Ingrese el valor de la base: "))

alto = int(input("Ingrese el valor de la altura: "))
while alto <= 0:
    print("Debe ingresar un valor positivo")
    alto = int(input("Ingrese el valor de la altura: "))

ancho = int(input("Ingrese el valor de la altura: "))
while ancho <= 0:
    print("Debe ingresar un valor positivo")
    ancho = int(input("Ingrese el valor de la altura: "))
    
#creando objeto de la clase
caja1 = Caja(largo,ancho,alto)
print(caja1.calcularVolumen())
caja2 = Caja(2,4,3)
print(caja2.calcularVolumen())
