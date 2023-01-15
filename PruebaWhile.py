import math

numero = int(input ("Introduce numero: "))

intentos = 0

while numero < 0:
    print ("numero negativo.....")

    if intentos == 2:
        print ("Demasiados intentos")
        break;
    
    numero = int(input ("Introduce numero: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print (f"La raiz cuadarda de {numero} es {solucion}")