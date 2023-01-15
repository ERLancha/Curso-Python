import sqlite3 

miConexion = sqlite3.connect("BBDD/PrimeraBase")


miCursor=miConexion.cursor()


miCursor.execute("CREATE TABLE PRODUCTOS ( NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")




miConexion.close()