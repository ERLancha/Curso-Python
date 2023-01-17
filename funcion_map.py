#Aplica una funcion a cada uno de los elementos de una 
#lista iterable, devolviendo una lista nueva con los resultados

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpledados = [

    Empleado("Juan","Director", 75000),
    Empleado("Ana","Presidente", 85000),
    Empleado("Jose","Admninistrativo", 2500),
    Empleado("Mario","Botones", 400)

]

def calculo_comision(empleado):

    if empleado.salario <=6000:
        empleado.salario = empleado.salario * 1.03

    return empleado

listaEmpleadosConComision = map(calculo_comision, listaEmpledados)

for emp in listaEmpleadosConComision:
    print (emp)