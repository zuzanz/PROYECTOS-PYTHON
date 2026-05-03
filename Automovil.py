class Automovil:
    def __init__(self, marca,modelo,anio ):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def get_marca(self):
        return self._marca
    
    def set_marca(self, nuevo_marca):
        self._marca = nuevo_marca

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def get_anio(self):
        return self._anio
    
    def set_anio(self, nuevo_anio):
        self._anio = nuevo_anio

automovil = Automovil("Gaturro", "Galaxia", 2026)

print("=== Datos Iniciales ====")
print("Marca:", automovil.get_marca())
print("Modelo:", automovil.get_modelo())
print("Año:", automovil.get_anio())

automovil.set_marca("Cuy Magico")
automovil.set_modelo("Sheltie")
automovil.set_anio(2024)

print("\n=== Datos Actualizados ====")
print("Marca nueva Actualizada:", automovil.get_marca())
print("Modelo nueva Actualizada:", automovil.get_modelo())
print("Año nueva Actualizada:", automovil.get_anio())

