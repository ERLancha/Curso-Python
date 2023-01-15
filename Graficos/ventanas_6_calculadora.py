from tkinter import *

raiz = Tk()

raiz.title("Calculadora")


miFrame = Frame(raiz)

miFrame.pack()

valor = StringVar()
operacion = StringVar()
resultado = 0
calculoRealizado = False



def botonBorrarOperacion():
    valor.set("")
    operacion.set("")
    resultado = 0


def botonNumero(v):
    # print("Valor recogido :", v)
    global valor
    global calculoRealizado

    if not calculoRealizado:
        antiguo = valor.get()
        valor.set(antiguo + v)
    else:
        valor.set(v)

def botonOperacion(op):

    global resultado
    global valor
    global operacion
    global calculoRealizado

    calculoRealizado = False 

    operacion.set(op)

    if operacion.get() == "+" :
        resultado += float(valor.get())
        calculoRealizado = True
    elif operacion.get() == "x":
        if resultado == 0:
            resultado = float(valor.get())
        else:
            resultado*= float(valor.get())
        calculoRealizado = True
    elif operacion.get() == "-":
        if resultado == 0:
            resultado = float(valor.get())
        else:
            resultado -= float(valor.get())
        calculoRealizado = True
    elif operacion.get() == "/":
        if resultado == 0:
            resultado = float(valor.get())
        else:
            if float(valor.get()) != 0 :
                resultado = resultado / float(valor.get())
            else:  
                valor.set("Infinito")
                resultado = 0
        calculoRealizado = True
    
    if valor.get() != "Infinito":
        valor.set(resultado)

def botonIgual():
    global resultado
    global valor
    global operacion

    if operacion.get() == "+" :
        resultado += float(valor.get())
    elif operacion.get() == "x":
        resultado*= float(valor.get())
    elif operacion.get() == "-":
        resultado -= float(valor.get())
    elif operacion.get() == "/":
        if float(valor.get()) != 0 :
            resultado = resultado / float(valor.get())
    else:  
        valor.set("Infinito")
        resultado = 0
    
    if valor.get() != "Infinito":
        valor.set(resultado)
        resultado = 0
    calculoRealizado = True


#-------------- Pantalla
pantalla = Entry(miFrame,textvariable=valor)
pantalla.grid(row=1, column=1,padx=10, pady=10,columnspan=4)

pantalla.config(bg="black", fg="#03f943",justify="right")

#-------------- Primera fila botones
boton7 = Button(miFrame,text="7",width=3, command=lambda:botonNumero("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame,text="8",width=3, command=lambda:botonNumero("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame,text="9",width=3, command=lambda:botonNumero("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame,text="/",width=3, command=lambda:botonOperacion("/"))
botonDiv.grid(row=2, column=4)


#-------------- Segunda fila botones
boton4 = Button(miFrame,text="4",width=3, command=lambda:botonNumero("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame,text="5",width=3, command=lambda:botonNumero("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame,text="6",width=3, command=lambda:botonNumero("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame,text="*",width=3, command=lambda:botonOperacion("x"))
botonMult.grid(row=3, column=4)

#-------------- Tercera fila botones
boton3 = Button(miFrame,text="3",width=3, command=lambda:botonNumero("3"))
boton3.grid(row=4, column=1)
boton2 = Button(miFrame,text="2",width=3, command=lambda:botonNumero("2"))
boton2.grid(row=4, column=2)
boton1 = Button(miFrame,text="1",width=3, command=lambda:botonNumero("1"))
boton1.grid(row=4, column=3)
botonRest = Button(miFrame,text="-",width=3, command=lambda:botonOperacion("-"))
botonRest.grid(row=4, column=4)

#-------------- Cuarta fila botones
boton0 = Button(miFrame,text="0",width=3, command=lambda:botonNumero("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame,text=",",width=3, command=lambda:botonNumero(","))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame,text="=",width=3, command=botonIgual)
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame,text="+",width=3, command=lambda:botonOperacion("+"))
botonSum.grid(row=5, column=4)

#-------------- quinta fila botones
botonSum = Button(miFrame,text="C",width=3, command=botonBorrarOperacion)
botonSum.grid(row=6, column=1,columnspan=4,sticky="we")

raiz.mainloop()


