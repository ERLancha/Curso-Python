#con *args acepta cualquier número de argumentos
#con **kwargs acepta argumentos de la forma base=5
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        #Acciones adicionales
        print("vamos a realizar un calculo: ")
        funcion_parametro(*args, **kwargs)  
        #Accion adicional
        print("Calculo terminado")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2):

    print(num1+num2)

def resta(num1, num2):

    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):

    print (pow(base, exponente))


suma(7,5)

resta(12,10)

potencia(base=3, exponente=5)