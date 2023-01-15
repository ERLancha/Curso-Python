import pickle

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

coche1=vehiculos("Toyota","auris")         

coche2=vehiculos("Toyota","RAv4")  

coche3=vehiculos("Toyota","yoigo")  

coches = [coche1,coche3,coche3]

fichero = open("listaCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

fichero = open("listaCoches","rb")

misCoches = pickle.load(fichero)

fichero.close()

for p in misCoches:
    print (p.estado())