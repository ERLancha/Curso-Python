def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #Acciones adicionales
        print("vamos a realizar un calculo: ")
        funcion_parametro()
        #Accion adicional
        print("Calculo terminado")

    return funcion_interior

@funcion_decoradora
def suma():

    print(15+20)

def resta():

    print(30-10)

suma()

resta()