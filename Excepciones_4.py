def evaluaEdad(edad):

    if edad<0:
        raise TypeError("Edad no valida...")

    if edad<20:
        return "Joven"
    elif edad <30:
        return "madurito"
    elif edad <50:
        return "maduro del to"
    else:
        return "cuidate..."

try:
    print(evaluaEdad(-15))
except TypeError as errorMio:
    print("Error!!! \t" + str(errorMio))