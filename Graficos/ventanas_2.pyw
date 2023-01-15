from tkinter import *

raiz = Tk()


raiz.title("Ventana 1")

#ancho, alto
#raiz.resizable(False,False)

#raiz.geometry("800x600")

raiz.config(bg="red")

miFrame = Frame()

#miFrame.pack(side="bottom",anchor="e")

miFrame.pack(fill="both", expand="False")

miFrame.config(bg="blue")

miFrame.config(width="800", height="360")

miFrame.config(bd=35)

miFrame.config(relief="groove")

raiz.mainloop()