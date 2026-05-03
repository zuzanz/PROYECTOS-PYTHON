class TiendaJuego:
    def __init__(self,nombre_del_jugador, nombre_de_usuario, saldo):
        self._nombre_del_jugador = nombre_del_jugador
        self._nombre_del_usuario = nombre_de_usuario
        self._saldo = saldo

#get y sets
    def get_nombre_del_jugador(self):
        return self._nombre_del_jugador
    def set_nombre_del_jugador(self, nuevo_jugador):
        self._nombre_del_jugador = nuevo_jugador

    def get_nombre_del_usuario(self):
        return self._nombre_del_usuario
    def set_nombre_del_jugador(self, nuevo_usuario):
        self._nombre_del_usuario = nuevo_usuario

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo

#Metodos de cobro y saldo del jugador
    def comprar_juego(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Juego cobrado")
        else:
            self.sin_saldo()

    def sin_saldo(self):
            print("No tienes suficiente dinero para esta compra")

    def comprar_skin(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("compra realizada con exito")
        else:
            self.sin_saldo()

    def sin_saldo(self):
            print("No tienes suficiente dinero para esta compra")

    def recargar_saldo(self, monto):
        if monto > 0:
            self._saldo += monto
            print("Saldo recargado correctamente")
        else:
            print("Monto inválido")

    def mostrar_resultados(self):
        print("\n***DATOS DEL USUARIO ***")
        print("Nombre:", self._nombre_del_jugador)
        print("Correo:", self._nombre_del_usuario)
        print("Saldo:", int(self._saldo))

#sistema de pasaje escolar
nombre = input("Ingrese nombre: ")
correo = input("Ingrese usuario: ")
saldo = float(input("Ingrese saldo inicial: "))
#agregando la informacion del cliente para el usuario terminal
cliente = TiendaJuego(nombre, correo, saldo)

#funcion de recarga para el estudiante
cliente.comprar_juego(5990)
cliente.comprar_skin(2990)
cliente.recargar_saldo(10000)
#imprime los resultados del jugador
cliente.mostrar_resultados()