import re

nombre1="Sandra López"

nombre2="Antonio Gómez"

nombre3="María López"

#match busca al principio de la cadena
#search busca en toda la cadena de texto
"""
if re.match("Sandra",nombre1, re.IGNORECASE):
    print ("Encontrado")
else:
    print ("No encontrado")


cadena1 = "Pepito lopez"

cadena2 = "5465465464"

cadena3 = "25Pepita perez"

if re.match("\d",cadena1):
    print ("Encontrado")
else:
    print ("No encontrado")
"""

if re.search(".[oó]pez", nombre2):
    print ("Encontrado")
else:
    print ("No encontrado")



