#Herencia
class vehiculos():

    def __init__(self, marca, modelo):
        self.marca  = marca
        self.modelo = modelo
        self.enMarcha = False
        self.accelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def accelerar (self):
        self.accelera = True
    
    def frenar (self):
        self.frena = True

    def estado (self):
        print ("Marca: ", self.marca, "\nModelo : ", self.modelo, "\nAcelerando?: " ,
         self.accelera , "\nFrenando?: " , self.frena)


class Moto(vehiculos): #Hereda de la clase vehiculos
    hcaballito = ""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado (self): #sobreescribimos el método
        print ("Marca: ", self.marca, "\nModelo : ", self.modelo, "\nAcelerando?: " ,
         self.accelera , "\nFrenando?: " , self.frena, "\n", self.hcaballito)

class Furgoneta(vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La fugoneta no esta cargada"


class VElectricos():
    def __init__(self) -> None:
        self.autonomia = 100

    def cargarEnergia(self):        
        self.cargando = True

miMoto = Moto("Yamaha","ZX")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Express")

miFurgoneta.arrancar()

print (miFurgoneta.carga(True))

miFurgoneta.estado()

class BicicletaEletrica (vehiculos,VElectricos): #Herencia multiple
    pass


miBici = BicicletaEletrica("BH","HJ4523")

miBici.estado()