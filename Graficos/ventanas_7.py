from tkinter import *

raiz = Tk()

raiz.title("Ventana")

varOpcion = IntVar()

def valSeleccionado():

    print(varOpcion.get())

Label(raiz,text="Género: ").pack()

Radiobutton(raiz,text="Masculino",variable=varOpcion,value=1,command=valSeleccionado).pack()
Radiobutton(raiz,text="Femenino",variable=varOpcion,value=2,command=valSeleccionado).pack()  




raiz.mainloop()