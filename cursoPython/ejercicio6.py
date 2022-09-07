# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

import math


areaTriangulo = lambda altura, base : (base * altura) / 2

areaCirculo = lambda radio : math.pi * math.pow(radio, 2)

print("El area del triangulo es : ", areaTriangulo(4, 5))
print("El area del circulo es : " , round(areaCirculo(5),2))