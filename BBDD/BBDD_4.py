import sqlite3 

miConexion = sqlite3.connect("BBDD/GestionProductos")


miCursor=miConexion.cursor()

#Las tres comillas te permiten poner las ordenes en varias filas.... ains!!
#Se puede utilizar la clausula UNIQUE a los campos que no se puedan repetir y no 
#sean claves

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    '''
)

#Creamos una lista con los productos
productos = [
    ("pelota",20,"jugueteria"),
    ("pantalón",16,"confección"),
    ("destornillador",25,"ferreteria"),
    ("jarrón",45,"cerámica"),
]

miConexion.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
miConexion.commit()

miConexion.close()