# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numeroInicial = int(input("Ingresa un numero inicial: "))
numeroFinal = int(input("Ingresa un numero final: "))


range_1 = range(numeroInicial, numeroFinal)
list_1 = list()
for item in range_1:
    if item % 2 != 0:
        list_1.append(item)
print(list_1)




