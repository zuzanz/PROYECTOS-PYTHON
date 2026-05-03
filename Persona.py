class Persona:
    def __init__(self, nombre, edad, dirección):
        self._nombre = nombre
        self._edad = edad
        self._dirección = dirección

    def get_nombre(self):
     return self._nombre
    
    def set_nombre(self, nuevo_nombre):
       self._nombre = nuevo_nombre

    def get_edad(self):
     return self._edad
    
    def set_edad(self, nueva_edad):
       if nueva_edad >= 0:
          self._edad = nueva_edad
       else:
          print("La edad debe ser un número positivo.") 

    def get_dirección(self):
     return self._dirección
    
    def set_dirección(self, nueva_dirección):
       self.dirección = nueva_dirección

persona = Persona("Escarlet", 38, "cordova #1904")

print("Nombre:", persona.get_nombre())
print("Edad:", persona.get_edad())
print("Dirección:", persona.get_dirección())



persona.set_nombre("Luzi")
persona.set_edad(20)

print("Nombre actualizado:", persona.get_nombre())
print("Edad actualizado:", persona.get_edad())



 # pyright: ignore[reportUndefinedVariable]