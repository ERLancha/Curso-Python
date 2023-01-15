from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():

    fichero = filedialog.askopenfilename(title="Abrir Fichero", initialdir="C:",
      filetypes=(("Ficheros excel","*.xlsx"),
      ("Ficheros de texto","*.txt"),
      ("Validos","*.txt *.xlsx"),
      ("Todos","*.*")))

    print(fichero)


Button (raiz, text="Abrir fichero", command=abreFichero).pack()
raiz.mainloop()