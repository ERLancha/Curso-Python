import re

cadena="Vamos a aprender expresiones regulares"

textoBuscar="expresiones"

"""
if re.search(textoBuscar, cadena) is not None:
    print("Encontrado")
else:
    print("No Encontrado")
"""

textEncontrado = re.search(textoBuscar, cadena)

print(textEncontrado.start()) 
print(textEncontrado.end())
print(textEncontrado.span()) 

textoBuscar="e"

print(len(re.findall(textoBuscar, cadena)))