class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpledados = [

    Empleado("Juan","Director", 750000),
    Empleado("Ana","Presidente", 850000),
    Empleado("Jose","Admninistrativo", 25000),
    Empleado("Mario","Botones", 4000)

]

salarios_altos = filter(lambda empleado:empleado.salario>50000,
                         listaEmpledados)

for emp in salarios_altos:
    print (emp)