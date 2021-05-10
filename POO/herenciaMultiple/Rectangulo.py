from figuraGeometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)
        
    def __str__(self):
        return "RECTANGULO:\nAlto: " + str(self.getAlto()) +", Ancho: " + str(self.getAncho()) + ", Color: " + self.getColor()
    
    def area(self):
        return self.getAlto() * self.getAncho()