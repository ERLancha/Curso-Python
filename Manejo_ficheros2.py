from io import open

archivo_texto = open("archivo.txt","r")

print (archivo_texto.read())

archivo_texto.seek(5)

print (archivo_texto.read())

archivo_texto.seek(0)

archivo_texto.seek(len(archivo_texto.readline()))

print (archivo_texto.read())

archivo_texto.close()