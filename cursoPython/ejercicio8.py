# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(anio):
    if anio % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
    elif anio % 4 == 0 and anio % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")

esBisiesto(1900)
esBisiesto(2000)

