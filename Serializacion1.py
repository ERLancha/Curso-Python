import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

#borramos de la memoria el fichero
del (fichero_binario)


fichero = open("lista_nombres","rb")

lista = pickle.load(fichero)

print(lista)

fichero.close()

del (fichero)