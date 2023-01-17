#Utilizaremos la programación funcional
#La funcion filter comprueba que unos elementos de una lista cumplen cierto
#regla y devuelve aquellos elementos que lo cumplen.

def numero_par(num):

    if num % 2 == 0:
        return True

#creamos una lista
numeros=[17,24,7,39,8,92]

#filter devuelve un objeto lista
#print(list(filter(numero_par,numeros)))

#Utilizando una función lambda
print(list(filter(lambda numero_par2:numero_par2%2==0,numeros)))

