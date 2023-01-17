import sqlite3
from tkinter import messagebox

def conectar():

    global conexion
    
    conexion=sqlite3.connect("Practica_Guiada/Usuarios")


def crearBBDD():

    global conexion
    global cursor


    conexion=sqlite3.connect("Practica_Guiada/Usuarios")
    
    cursor=conexion.cursor()

    try:
        cursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100)
            )
            '''
        )

        messagebox.showinfo("BBDD", "BBDD creada!!")

        cursor.close()
    except:

        messagebox.showwarning("BBDD", "La BBDD ya existe")

def crear(nombre, passw, apellido, direccion, comentario):

    if not is_connected():
        conectar()
    try:
        """cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'"+nombre+
        "','"+passw+"','"+apellido+"','"+direccion+
        "','"+comentario+"')" )"""

        datos = nombre, passw, apellido, direccion, comentario
        cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)",(datos))
        
        conexion.commit()
        cursor.close()
    except Exception as Ex:
        messagebox.showerror("Creación de registro","No se ha grabado el registro ")


def leer(id):

    global cursor

    print ("Id a buscar : ", id)

    if not is_connected():
        conectar()

    try:    
        cursor.execute("SELECT NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION , COMENTARIOS FROM DATOSUSUARIOS WHERE ID = "+ id)

        resultado = cursor.fetchall()

        conexion.commit()

        cursor.close()
        return resultado
    except:
        messagebox.showerror("BBDD", "Error al buscar registro")

def actualizar(id,nombre, passw, apellido, direccion, comentario):

    global cursor

    nuevosValores = ""

    idInt = int(id)

    if not type(idInt) is int:
        raise TypeError("ERROR(TypeError): Solo se permiten enteros como ids")

    if nombre != "" and len(nuevosValores) == 0:
        nuevosValores = nuevosValores + "SET NOMBRE_USUARIO= '" + nombre + "'"
    else:
        nuevosValores = nuevosValores + ", NOMBRE_USUARIO= '" + nombre  + "'"
    
    if passw != "" and len(nuevosValores) == 0:
        nuevosValores = nuevosValores + "SET PASSWORD= '" + passw + "'"
    else:
        nuevosValores = nuevosValores + ", PASSWORD= '" + passw + "'"

    if apellido != "" and len(nuevosValores) == 0:
        nuevosValores = nuevosValores + "SET APELLIDO= '" + apellido + "'"
    else:
        nuevosValores = nuevosValores + ", APELLIDO= '" + apellido + "'"

    if direccion != "" and len(nuevosValores) == 0:
        nuevosValores = nuevosValores + "SET DIRECCION= '" + direccion + "'"
    else:
        nuevosValores = nuevosValores + ", DIRECCION= '" + direccion + "'"

    if comentario != "" and len(nuevosValores) == 0:
        nuevosValores = nuevosValores + "SET COMENTARIOS= '" + comentario + "'"
    else:
        nuevosValores = nuevosValores + ", COMENTARIOS= '" + comentario + "'"

    sqlUpdate = "UPDATE DATOSUSUARIOS "

    sqlWhere = " WHERE ID = " + id

    if len(nuevosValores) > 0:
        sqlUpdate = sqlUpdate + nuevosValores + sqlWhere

    if not is_connected():
        conectar()
    try:
        print("acualizar: \n",sqlUpdate)
        cursor.execute(sqlUpdate)

        conexion.commit()
        cursor.close()
    except Exception as Ex:
        messagebox.showerror("Actualizacion de registro","No se ha actualizado el registro el registro ")

def eliminar(id):

    global cursor

    idInt = int(id)

    if not type(idInt) is int:
        raise TypeError("ERROR(TypeError): Solo se permiten enteros como ids")

    sql = "DELETE FROM DATOSUSUARIOS WHERE ID = " + id

    if not is_connected():
        conectar()
    try:
        print("Borrar: \n",sql)
        cursor.execute(sql)

        conexion.commit()
        cursor.close()
    except Exception as Ex:
        messagebox.showerror("Creación de registro","No se ha grabado el registro " + Ex)


def is_connected():
    global conexion
    global cursor

    try:
        conexion=sqlite3.connect("Practica_Guiada/Usuarios")
        cursor=conexion.cursor()
        print ("Conectado...")        
        return True
    except Exception as ex:
        print ("No Conectado...")
        return False

def desconectar():
    global conexion
    global cursor

    if is_connected():
        cursor.close()
        conexion.close()

        print("BBDD desconectada")