edad = input("Introduce edad: ")

while (edad.isdigit() == False):
    print ("Error....")
    edad = input ("Introduce edad: ")



print ("La edad es: ", edad.upper())

nombre = input ("Introduce nombre : ")

print ("El nombre es : ", nombre.capitalize())