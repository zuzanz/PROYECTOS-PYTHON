class Cafeteria:
    def __init__(self, nombredelcliente, correo, saldo):
        self._nombredelcliente = nombredelcliente
        self._correo = correo
        self._saldo = saldo
    
    # GET Y SET DE CAFETERIA
    def get_nombredecliente(self):
        return self._nombredelcliente
    def set_nombredecliente(self, nuevo_nombredecliente):
        self._nombredelcliente = nuevo_nombredecliente

    def get_correo(self):
        return self._correo
    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
    
    #nuevas opciones para pagos de productos
    def comprar_cafe(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Compra de café realizada")
        else:
            print("Saldo insuficiente")

    def comprar_sandwich(self, precio):
        if self._saldo >= precio:
            self._saldo -= precio
            print("Compra de sandwish realizada")
        else:
            print("Saldo insuficiente")

    def recargar_saldo(self, monto):
        if monto > 0:
            self._saldo += monto
            print("Saldo recargado correctamente")
        else:
            print("Monto inválido")
        
    def mostrar_resultados(self):
        print("\n***DATOS DEL CLIENTE ***")
        print("Nombre:", self._nombredelcliente)
        print("Correo:", self._correo)
        print("Saldo:", int(self._saldo))

    #PROGRAMA PARA EL USUARIO
nombre = input("Ingrese nombre: ")
correo = input("Ingrese correo: ")
saldo = float(input("Ingrese saldo inicial: "))

cliente = Cafeteria(nombre, correo, saldo)

#PRECIOS DE LA CAFETERIA para agregar al cliente
cliente.comprar_cafe(1000)
cliente.comprar_sandwich(2000)
cliente.recargar_saldo(5000)

cliente.mostrar_resultados()



    