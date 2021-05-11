from producto import Producto
from orden import Orden

producto1 = Producto("Tornillo", 100)
producto2 = Producto("Grampa", 50)
producto3 = Producto("Cuchillo", 20)

productos = [producto1, producto2]

orden1 = Orden(productos)
print(orden1)
print(orden1.calcularTotal())

orden2 = Orden(productos)
orden2.agregarProducto(producto3)
print(orden2)
#print(orden2.calcularTotal())
print(orden1)
#print(orden1.calcularTotal())
