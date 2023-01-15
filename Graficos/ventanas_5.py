from tkinter import *

raiz = Tk()


raiz.title("Ventana 1")


miFrame = Frame(raiz,width=1200,height=400)

miFrame.pack()

nombre =StringVar()


Label(miFrame,text="Nombre : ").grid(row=0, column=0,sticky="e", padx=15, pady=10)
cuadroNombre=Entry(miFrame, textvariable=nombre)
cuadroNombre.grid(row=0, column=1, padx=15, pady=10)
cuadroNombre.config(fg="red")

Label(miFrame,text="Password : ").grid(row=1, column=0,sticky="e", padx=15, pady=10)
cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=15, pady=10)
cuadroPassword.config(show="*")

Label(miFrame,text="Apellidos : ").grid(row=2, column=0,sticky="e", padx=15, pady=10)
cuadroApellidos=Entry(miFrame)
cuadroApellidos.grid(row=2, column=1, padx=15, pady=10)

Label(miFrame,text="Direccion : ").grid(row=3, column=0,sticky="e", padx=15, pady=10)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=15, pady=10)

Label(miFrame,text="Comentario: ").grid(row=4, column=0,sticky="e", padx=15, pady=10)
cuadroComentario=Text(miFrame,width=16,height=5)
cuadroComentario.grid(row=4, column=1, padx=15, pady=10)


scrollComentarioVertical = Scrollbar(miFrame,command=cuadroComentario.yview)
scrollComentarioVertical.grid(row=4, column=2 , sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollComentarioVertical.set)

def codigoBoton():
    nombre.set("Juan")

boton = Button(raiz, text="Envio", command=codigoBoton)
boton.pack()



raiz.mainloop()


