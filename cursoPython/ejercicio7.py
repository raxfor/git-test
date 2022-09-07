# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(num):
    for item in range(2, num):
        if num % item == 0:
            return "No es primo"
    return "Es primo"

resultado = esPrimo(89)
print(resultado)


