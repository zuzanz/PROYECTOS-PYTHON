class Estudiante:
    def __init__(self,rut,nombre,carrera,semestre):
        self._rut = rut
        self._nombre = nombre
        self._carrera = carrera
        self._semestre = semestre

    def get_rut(self):
        return self._rut
    
    def set_rut(self,nuevo_rut):
        self._rut = nuevo_rut

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_carrera(self):
        return self._carrera
    
    def set_carrera(self,nuevo_carrera):
        self._carrera = nuevo_carrera

    def get_semestre(self):
        return self._semestre
    
    def set_semestre(self,nuevo_semestre):
        self._semestre = nuevo_semestre

estudiante = Estudiante("13600390-2", "Felipe","Informatica",4)

print("=== Datos Iniciales ====")
print("Rut:", estudiante.get_rut())
print("Nombre:", estudiante.get_nombre())
print("Carrera:", estudiante.get_carrera())
print("Semestre:", estudiante.get_semestre())

estudiante.set_rut("25700289-1")
estudiante.set_nombre("Nando")
estudiante.set_carrera("Informatica")
estudiante.set_semestre(7)

print("\n=== Nuevos Datos Actualizados ===")
print("Rut actualizado:", estudiante.get_rut())
print("Nombre actualizado:", estudiante.get_nombre())
print("Carrera actualizado:", estudiante.get_carrera())
print("Semestre actualizado:", estudiante.get_semestre())

