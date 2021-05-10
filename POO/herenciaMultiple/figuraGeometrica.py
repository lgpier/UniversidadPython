#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        self.__ancho = ancho 
        self.__alto = alto
    
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return "Ancho: " + str(self.ancho) + ", Alto: " + str(self.alto)
        
    def getAncho(self):
        return self.__ancho
    
    def getAlto(self):
        return self.__alto
    
    def setAncho(self,ancho):
        self.__ancho = ancho
        
    def setAlto(self,alto):
        self.__alto = alto
        