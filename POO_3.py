#Encapsulación
class Coche ():

    def __init__(self): #Constructor
        self.__largoChasis=250 #Propiedades encapsuladas utilizando dos guiones bajos
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        resultado = self.__chequeo()

        if resultado and self.__enMarcha:
            return "Arrancado"
        elif self.__enMarcha and not resultado:
            return "Algo ha ido mal"
        else:
            return "Parado"
    
    def estado(self):
        print ("El coche tiene ", self.__ruedas, " ruedas y un chasis de ", self.__anchoChasis, " cms ")

    def __chequeo(self): #Método encapsulado
        print ("Chequeando...")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()

print (miCoche.arrancar(True))

miCoche.estado()

print ("________")

miCoche2 = Coche()

print (miCoche2.arrancar(False))

miCoche2.estado()