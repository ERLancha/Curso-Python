from tkinter import *
from tkinter import messagebox
import sqlite3
import BBDD

root = Tk()

global id
global nombre
global apellido
global passw
global direccion

id = StringVar()
nombre = StringVar()
apellido = StringVar()
passw = StringVar()
direccion = StringVar()


#------------ Funciones -------------------------------------

def salirAplicacion():

    resp = messagebox.askyesno("Aviso", "¿Desea salir de la aplicación?")
    
    if resp == TRUE:
        BBDD.desconectar()
        root.destroy()

def borrarCampos():

    id.set("")
    nombre.set("")
    passw.set("")
    apellido.set("")
    direccion.set("")
    textoComentario.delete(1.0, END)

def crearRegistros():

    try:
        BBDD.crear(nombre.get(), passw.get(), apellido.get(), direccion.get(), textoComentario.get(1.0, END))
        messagebox.showinfo("Nuevo Registro","El registro se ha creado correctamente")
        borrarCampos()
    except Exception as e:
        print(e)
        messagebox.showerror("Nuevo Registro","Ha ocurrido un error al añadir registro")


def leerRegistro():

    try:
        resultado = BBDD.leer(id.get())

        print (resultado[0][0])

        nombre.set(resultado[0][0])
        passw.set(resultado[0][1])
        apellido.set(resultado[0][2])
        direccion.set(resultado[0][3])
        textoComentario.insert(1.0, resultado[0][4])

        
    except Exception as e:
        print(e)
        messagebox.showerror("Leer Registro","Ha ocurrido un error al leer registro \n")


def actualizarRegistros():

    try:
        BBDD.actualizar(id.get(),nombre.get(), passw.get(), apellido.get(), direccion.get(), textoComentario.get(1.0, END))
        messagebox.showinfo("Actualizar Registro","El registro se ha actualizado correctamente")
        borrarCampos()
    except Exception as e:
        print(e)
        messagebox.showerror("Actualizar Registro","Ha ocurrido un error al actualizar registro" )

def borrarRegistros():

    try:
        BBDD.eliminar(id.get())
        messagebox.showinfo("Borrar Registro","El registro se ha borrado correctamente")
        borrarCampos()
    except Exception as e:
        print(e)
        messagebox.showerror("Borrar Registro","Ha ocurrido un error al borrar el registro" )

#------------------------ Menu ------------------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

menuBBDD = Menu(barraMenu, tearoff=0)
menuBBDD.add_command(label="Conectar",command=lambda:BBDD.crearBBDD())
menuBBDD.add_command(label="Salir", command= lambda:salirAplicacion())

menuBorrar = Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label="Borrar Campos",command=borrarCampos)

menuCRUD = Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Crear",command=crearRegistros)
menuCRUD.add_command(label="Leer",command=leerRegistro)
menuCRUD.add_command(label="Actualizar", command=actualizarRegistros)
menuCRUD.add_command(label="Borrar",command=borrarRegistros)

menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=menuBBDD)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)


#------------------ Frame Principal ------------------

framePrincipal = Frame(root)

framePrincipal.pack()


cuadroID = Entry(framePrincipal, textvariable=id)
cuadroID.grid(row=0, column=1, padx=10, pady= 10)

cuadroNombre = Entry(framePrincipal, textvariable=nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady= 10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass = Entry(framePrincipal, textvariable=passw)
cuadroPass.grid(row=2, column=1, padx=10, pady= 10)
cuadroPass.config(show="?")

cuadroApellido = Entry(framePrincipal, textvariable=apellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady= 10)

cuadroDir = Entry(framePrincipal, textvariable=direccion)
cuadroDir.grid(row=4, column=1, padx=10, pady= 10)

textoComentario = Text(framePrincipal,width=16,height=5)
textoComentario.grid(row=5,column=1)
scrollVert=Scrollbar(framePrincipal, command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert)

idLabel = Label(framePrincipal, text="ID: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady= 10)

nombreLabel = Label(framePrincipal, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady= 10)

passLabel = Label(framePrincipal, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady= 10)

apellidoLabel = Label(framePrincipal, text="Apellidos: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady= 10)

direccionLabel = Label(framePrincipal, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady= 10)

comentarioLabel = Label(framePrincipal, text="Comentarios: ")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady= 10)

#-------------------- segundo frame ----------------------

botonesFrame = Frame(root)
botonesFrame.pack()

botonCrear=Button(botonesFrame,text="Crear",command=crearRegistros)
botonCrear.grid(row=0,column=0,sticky="e", padx=10, pady=10)

botonLeer=Button(botonesFrame,text="Leer",command=leerRegistro)
botonLeer.grid(row=0,column=1,sticky="e", padx=10, pady=10)

botonActualizar=Button(botonesFrame,text="Actualizar", command=actualizarRegistros)
botonActualizar.grid(row=0,column=2,sticky="e", padx=10, pady=10)

botonBorrar=Button(botonesFrame,text="Borrar",command=borrarRegistros)
botonBorrar.grid(row=0,column=3,sticky="e", padx=10, pady=10)


root.mainloop()