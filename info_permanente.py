import pickle

class persona:

    def __init__(self, nombre, genero, edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print ("Nueva persona : ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    personas=[]

    def __init__(self) -> None:
        listaDePersonas=open("ficheroExterno","ab+")

        listaDePersonas.seek(0)

        try: 
            self.personas = pickle.load(listaDePersonas)
            print ("Se han cargado {} personas ".format(len(self.personas)))

        except:
            print ("El fichero esta vacio")
        
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
            
    def addPersonas(self, p):
        self.personas.append(p)
        self.savePersonas()

    def showPersonas(self):
        for p in self.personas:
            print (p)

    def savePersonas(self):
        ListaPersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,ListaPersonas)

        ListaPersonas.close()
        del(ListaPersonas)


    def showInfoFichero(self):
        print ("Info del fichero : \n")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

p=persona("Antonio", "masculino","29")

miLista.addPersonas(p)

miLista.showInfoFichero()
"""
p=persona("Sandra", "fenmenino","29")

miLista.addPersonas(p)

p=persona("Maria", "fenmenino","9")

miLista.addPersonas(p)

p=persona("Antonio", "masculino","18")

miLista.addPersonas(p)

miLista.showPersonas()
"""



