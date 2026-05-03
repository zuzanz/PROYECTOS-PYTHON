class TarjetaEscolar:
    def __init__(self, nombre_del_estudiante, curso, saldo):
        self._nombre_del_estudiante = nombre_del_estudiante
        self._curso = curso
        self._saldo = saldo 

#get y sets
    def get_nombre_del_estudiante(self):
        return self._nombre_del_estudiante
    def set_nombre_del_cliente(self, nuevo_estudiante):
        self._nombre_del_estudiante = nuevo_estudiante

    def get_curso(self):
        return self._curso
    def set_curso(self, nuevo_curso):
        self._curso = nuevo_curso

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo

#funciones del sistema recarga escolar y cobro
    def pagar_pasaje(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Pasaje cobrado")
        else:
            self.sin_saldo()

    def sin_saldo(self):
            print("No tienes dinero suficiente para pagar el pasaje")

    def recargar_saldo(self, monto):
        if monto > 0:
            self._saldo += monto
            print("Saldo recargado correctamente")
        else:
            print("Monto inválido")

    def mostrar_resultados(self):
        print("\n***DATOS DEL ESTUDIANTE ***")
        print("Nombre:", self._nombre_del_estudiante)
        print("Correo:", self._curso)
        print("Saldo:", int(self._saldo))

#sistema de pasaje escolar
nombre = input("Ingrese nombre: ")
correo = input("Ingrese correo: ")
saldo = float(input("Ingrese saldo inicial: "))

cliente = TarjetaEscolar(nombre, correo, saldo)

#funcion de recarga para el estudiante
cliente.pagar_pasaje(260)
cliente.recargar_saldo(2000)
cliente.pagar_pasaje(260)

cliente.mostrar_resultados()

