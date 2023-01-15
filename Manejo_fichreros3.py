from io import open

archivo_texto = open("archivo.txt","r+")

archivo_texto.write("Comienzo")

lista_texto = archivo_texto.readlines()

lista_texto[1]="Esta linea desde la lista \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()