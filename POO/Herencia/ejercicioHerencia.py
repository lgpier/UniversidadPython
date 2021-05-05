class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+ ", velocidad: " + str(self.velocidad) + "Km/s"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__()+ ", tipo: " + self.tipo
    
vehiculo = Vehiculo("Rojo" , 4)
print(vehiculo)

coche = Coche("Verde", 4, 100)
print(coche)

bicicleta = Bicicleta("Amarilla",2,"Gravel")
print(bicicleta)