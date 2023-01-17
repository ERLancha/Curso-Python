
"""Solo para funciones que no sean complejas"""
area_triangulo=lambda base,altura:(base*altura)/2


print(area_triangulo(7,5))

print(area_triangulo(6,4))

destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_ana=13000

print(destacar_valor(comision_ana))