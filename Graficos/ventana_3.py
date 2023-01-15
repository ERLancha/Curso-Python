from tkinter import *

raiz = Tk()


raiz.title("Ventana 1")

#ancho, alto
#raiz.resizable(False,False)

#raiz.geometry("800x600")

raiz.config(bg="blue")

miFrame = Frame(raiz,width=500,height=400)

miLabel=Label(miFrame, text="hola a todo el mundo!!!")

miFrame.pack()
  
miLabel.place(x=200, y=200)

Label(miFrame, text="hola a todo el mundo!!!",fg="blue", font=("Arial",18)).place(x=200, y=100)

miImagen=PhotoImage(file="./Graficos/aikido_lego.png",height=80,width=80,format=)

Label(miFrame,image=miImagen).place(x=10,y=20)

raiz.mainloop()