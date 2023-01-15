from tkinter import *

raiz = Tk()

raiz.title("Ventana")

playa = IntVar()
montana = IntVar()
rural = IntVar()


def opcionesViaje():

    opcionEscogida = ""

    if (playa.get()==1):
        opcionEscogida+=" playa"
    if (montana.get()==1):
        opcionEscogida+=" montaña"
    if (rural.get()==1):
        opcionEscogida+=" rural"
    
    texto.config(text=opcionEscogida)

Label(raiz,text="Destinos: ").pack()

Checkbutton(raiz,text="Playa",variable=playa, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(raiz,text="Montaña",variable=montana,onvalue=1, offvalue=0,command=opcionesViaje).pack()  
Checkbutton(raiz,text="Rural",variable=rural,onvalue=1, offvalue=0,command=opcionesViaje).pack()

texto = Label(raiz)
texto.pack()

raiz.mainloop()