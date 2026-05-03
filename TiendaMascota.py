class TiendaMascota:
    def __init__(self,cliente_pet, correo, saldo):
        self._cliente_pet = cliente_pet
        self._correo = correo
        self._saldo = saldo

    def get_cliente_pet(self):
        return self._cliente_pet
    def set_cliente_pet(self, nuevo_cliente_pet):
        self._cliente_pet = nuevo_cliente_pet
    
    def get_correo(self):
        return self._correo
    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo

    def comprar_comida(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Juego cobrado")
        else:
            self.sin_saldo()

    def sin_saldo(self):
            print("No tienes suficiente dinero para esta compra")


    def comprar_juguetes(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Juego cobrado")
        else:
            self.sin_saldo()

    def sin_saldo(self):
            print("No tienes suficiente dinero para esta compra")

    def recarga_saldo(self,precio):
        if self._saldo >= precio:
          self._saldo += precio
          print("Su recarga se hizo efectiva")
        else:
          print("Monto ingresado incorrecto")

    def mostrar_resultados(self):
        print("\n*** Datos personales del cliente ***")
        print("Nombre:", self._cliente_pet)
        print("Correo:", self._correo)
        print("Saldo:", int(self._saldo))

nombre = input("Ingrese Nombre:")
correo = input("INgrese correo:")
saldo = float(input("Ingrese saldo inicial: "))

cliente = TiendaMascota(nombre, correo, saldo)

cliente.comprar_comida(1000)
cliente.comprar_juguetes(6000)
cliente.comprar_comida(10000)
cliente.mostrar_resultados()


       

