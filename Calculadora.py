 #Defino la Clase Llamada Calculadora
class Calculadora:
    #Defino sus atributos y creo su contructor
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
    #metodo Get y Set para el Numero 1
    def get_num1(self):
        return self._num1
    
    def set_num1(self, valor):
        self._num1 = valor
    #Metodo Get y Set para el Numero 2
    def get_num2(self):
        return self._num2
    
    def set_num2(self, valor):
        self._num2 = valor


    #Creo Metodos Normales para cada operacion
    def sumar(self):
        return self._num1 + self._num2
    def restar(self):
        return self._num1 - self._num2
    def division(self):
        return self._num1 / self._num2
    def multiplicacion(self):
        return self._num1 * self._num2

    #Creo un Metodo Customer para el Cliente que vera la info
    def mostrar_resultados(calculadora):

        #Obtener información de la calculadora
        num1 = calculadora.get_num1()
        num2 = calculadora.get_num2()
        #Realizar operaciones
        resultado_suma = calculadora.sumar()
        resultado_resta = calculadora.restar()
        resultado_division = calculadora.division()
        resultado_multiplicacion = calculadora.multiplicacion()
        #Mostrar información
        print("--- Información de la calculadora ---")
        print("Número 1:", num1)
        print("Número 2:", num2)
        #Mostrar resultados en diferentes formas con print
        print("\n--- Resultados de las operaciones ---")
        print("Resultado de la suma: {}".format(resultado_suma))
        print("Resultado de la resta:", repr(resultado_resta))
        print(f"Resultado de la division: {resultado_division}")
        print("Resultado de la multiplicacion:" + str(resultado_multiplicacion))

#Instancia
calculadora = Calculadora(5, 5)
calculadora.mostrar_resultados()


"""
    Comentario de Bloque

"""

'''

'''