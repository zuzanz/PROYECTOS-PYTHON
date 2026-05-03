class Producto:
    def __init__(self,código,nombre,precio,categoría):
        self._código = código
        self._nombre = nombre
        self._precio = precio
        self._categoría = categoría

    def get_código(self):
        return self._código

    def set_código(self, nuevo_código):
        self._código = nuevo_código

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio debe ser numero positivo")
                             
    def get_categoría(self):
        return self._categoría

    def set_categoría(self, nuevo_categoría):
        self._categoría = nuevo_categoría

producto = Producto("001", "Maní", 1990, "Frutos secos")

print("=== Datos iniciales ===")
print("Codígo:", producto.get_código())
print("Nombre:", producto.get_nombre())
print("Precio:", producto.get_precio())
print("Categoría:", producto.get_categoría())

producto.set_código("002")
producto.set_nombre("Jamon")
producto.set_precio(3400)
producto.set_categoría("Embutido")

print("\n=== Productos Actualizados ===")
print("Codígo:", producto.get_código())
print("Nombre:", producto.get_nombre())
print("Precio:", producto.get_precio())
print("Categoría:", producto.get_categoría())

