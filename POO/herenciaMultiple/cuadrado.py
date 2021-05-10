from figuraGeometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def __str__(self):
        return "CUADRADO:\nLado: " + str(self.getAncho()) + ", Color: " + self.getColor()
    
    def area(self):
        return self.getAlto() * self.getAncho()
    
        
        