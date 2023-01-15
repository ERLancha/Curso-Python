from tkinter import *

raiz = Tk()

raiz.title("Ventana")

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

archivoMenu =Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Gurardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")



edicionMenu =Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


herramientasMenu =Menu(barraMenu,tearoff=0)

ayudaMenu =Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas",menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)


raiz.mainloop()