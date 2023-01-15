import sqlite3 

miConexion = sqlite3.connect("BBDD/PrimeraBase")


miCursor=miConexion.cursor()
'''
Grabar varios productos
variosProductos = [
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camion",20,"Juguetes")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miConexion.commit()
'''
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print("Nombre articulo : " , producto[0], " Sección : " , producto[2] )



miConexion.close()