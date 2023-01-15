import sqlite3 

miConexion = sqlite3.connect("BBDD/GestionProductos")


miCursor=miConexion.cursor()

#Las tres comillas te permiten poner las ordenes en varias filas.... ains!!
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    '''
)

#Creamos una lista con los productos
productos = [
    ("AR01","pelota",20,"jugueteria"),
    ("AR02","pantalón",16,"confección"),
    ("AR03","destornillador",25,"ferreteria"),
    ("AR04","jarrón",45,"cerámica"),
]

miConexion.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)
miConexion.commit()

miConexion.close()