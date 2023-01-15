#Principio de sustitució isinstance()
#super()

class Persona():

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad)


class Empleado(Persona):

    def __init__(self, nombre, edad, salario) -> None:
        super().__init__(nombre, edad)

        self.salario = salario

    def descripcion(self):
        super().descripcion()        
        print ("Salario: ", self.salario)

uno = Empleado("Jose",34,2345)

uno.descripcion()

print ("Es empleado :", isinstance(uno,Empleado))


