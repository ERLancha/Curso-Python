class Coche ():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            return "Arrancado"
        else:
            return "Parado"


miCoche = Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("estado? ", miCoche.estado())

miCoche.arrancar()

print("estado? ", miCoche.estado())