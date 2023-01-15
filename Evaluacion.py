
print("SALUDOS HUMANO...")

nota_alumno = int(input("Indroduzca nota del alumno: "))
'''
def evaluacion(nota):
    if nota < 5:
        valoracion = "suspenso"
    elif nota < 0 or nota > 10:
        valoracion = "Repite la nota"
    else:
        valoracion = "aprobado"
    return valoracion

'''
def evaluacion(nota):
    if 0<nota< 10:
        if 0<nota < 5:
            valoracion = "Suspenso"
        else:
            valoracion = "aprobado"
    else:
            valoracion = "repite la nota"
    return valoracion

print (evaluacion(nota_alumno))