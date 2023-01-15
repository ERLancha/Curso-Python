def devuelveCiudades (*ciudades): #Con el * acepta un número indeterminado de párametros
    for i in ciudades:
        for subElemento in i:
            yield subElemento
            

ciudadesDevuetas=devuelveCiudades("Madrid","Paris","Londres")

print(next(ciudadesDevuetas))

print(next(ciudadesDevuetas))

#Utilizamos la orden yield from para evitar bucles anidados.....

def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudadesDevueltas2 = devuelveCiudades2("Madrid","Paris","Londres")

print(next(ciudadesDevueltas2))

print(next(ciudadesDevueltas2))





