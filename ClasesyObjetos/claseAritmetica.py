class Aritmetica:
    """Clase Aritmetica para realizar las operaciones de 
    suma, resta, etc."""
    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operacion con los atributos
        de la clase"""
        return self.operando1 + self.operando2
    
#creando un objeto
aritmetica = Aritmetica(2,4)
print("Resultado de la suma: ", aritmetica.sumar())
