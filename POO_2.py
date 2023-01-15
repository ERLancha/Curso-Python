class Coche ():

    def __init__(self): #Constructor
        self.__largoChasis=250 #Propiedades encapsuladas utilizando dos guiones bajos
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            return "Arrancado"
        else:
            return "Parado"
    
    def estado(self):
        print ("El coche tiene ", self.__ruedas, " ruedas y un chasis de ", self.__anchoChasis, " cms ")


miCoche = Coche()

print (miCoche.arrancar(True))

miCoche.estado()

