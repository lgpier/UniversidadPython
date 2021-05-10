from cuadrado import Cuadrado
from Rectangulo import Rectangulo
from figuraGeometrica import FiguraGeometrica

#No es posible crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica()

cuadrado = Cuadrado(4, "Azul")
rectangulo = Rectangulo(4, 2, "Verde")

print(cuadrado)
print(cuadrado.area())
print(cuadrado.getAlto())
print(cuadrado.getAncho())
print(cuadrado.getColor())
print("------------------")
print(rectangulo)
print(rectangulo.area())
print(rectangulo.getAlto())
print(rectangulo.getAncho())
print(rectangulo.getColor())

#Method Resolution Order
#print(Cuadrado.mro())