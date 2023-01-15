from tkinter import *
from tkinter import messagebox

raiz = Tk()

raiz.title("Ventana")

def infoAdicional():
    messagebox.showinfo ("Ventana ayuda", "Ventana de ayuda en Python")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto sin licencia")

def avisoSalir():
    opcion = messagebox.askquestion("Salir", "¿Salir?")

    if opcion == messagebox.YES:
        raiz.destroy()

def cerrarDocumento():
    opcion = messagebox.askretrycancel("Reintentar", "*¿Desea reintentar?")
    
    if opcion == FALSE:
        raiz.destroy()


barraMenu = Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

archivoMenu =Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Gurardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=avisoSalir)



edicionMenu =Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


herramientasMenu =Menu(barraMenu,tearoff=0)

ayudaMenu =Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de ...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas",menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)


raiz.mainloop()