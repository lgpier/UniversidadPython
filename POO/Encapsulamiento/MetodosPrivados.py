class Persona:
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno):
        self.nombre = nombre
        # _ significa protected: Se puede acceder directamente o desde los métodos get o set. Lo correcto es usar los getters and setters
        self._apellidoPaterno = apellidoPaterno
        # __ significa privado
        self.__apellidoMaterno = apellidoMaterno
    
    def metodoPublico(self):
        self.__metodoPrivado()
        
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellidoPaterno)
        print(self.__apellidoMaterno)
    
    def getapellidoMaterno(self):
        return self.__apellidoMaterno
    
    def setapellidoMaterno(self,apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno
    
p1 = Persona("Lucas","Piersanti","Manduca")
#p1.metodoPrivado() No se puede llamar directamente pq es metodo privado
p1.metodoPublico()
print("")
print(p1.nombre)
print(p1._apellidoPaterno)
print(p1.getapellidoMaterno())
