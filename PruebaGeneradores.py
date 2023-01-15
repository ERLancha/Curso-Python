#Estruturas que extraen valores de una función y los convierten en objetos iterables.
'''
def nombFuncion():
    yield valor
'''

def generaNumerosPares(limite):
    num = 1
    miLista = []

    while num<limite:
        miLista.append(num*2)

        num+=1

    return miLista

print (generaNumerosPares(10))

def generaNumerosPares2(limite):
    num = 1
    while num < limite:
        yield num * 2
        num+=1
    
devuelvePares = generaNumerosPares2(10)

print (next(devuelvePares))

print ("Siguiente par...")

print (next(devuelvePares))

print ("Fin....")

