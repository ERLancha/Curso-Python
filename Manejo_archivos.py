from io import open

archivo_texto =open("archivo.txt","w")

frase = "hoooooola \n a todos"

archivo_texto.write(frase)

archivo_texto.close()


archivo_texto = open("archivo.txt","r")

texto = archivo_texto.read()

archivo_texto.close()

print (texto)

archivo_texto = open ("archivo.txt","r")

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])


archivo_texto = open ("archivo.txt","a")

archivo_texto.write("\n eeeeoooo!")

archivo_texto.close()



