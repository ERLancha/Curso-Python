def divide ():

    try:
        op1= float(input("Primer numero: "))

        op2= float(input("Segundo numero: "))

        print ("Se divide...: " +str(op1/op2))
    
    except ValueError:
        print ("El valor no es correcto")

    except ZeroDivisionError:
        print ("No se divide entre 0")
        
    finally:
        print ("Fin")

divide()
