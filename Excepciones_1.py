def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print ("No se puede dividir por cero")
        return ("Operación erronea")
while True:
    try:
        op1 = (int(input("Primer numero: ")))
        op2 = (int(input("Segundo numero: ")))
        break
    except ValueError:
        print ("Se necesita entero")    

print(divide(op1, op2))

