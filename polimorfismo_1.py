class Coche():

    def desplazamiento(self):
        print ("Cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print ("Dos ruedas")

class Camion():

    def desplazamiento(self):
        print ("Seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)

