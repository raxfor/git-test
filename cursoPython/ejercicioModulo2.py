# Importamos el módulo time para poder coger la hora.
import time

# Inicializamos las variables
hour = time.strftime('%H')
minutes = time.strftime('%M')

# Comprobamos si la hora es mayor o igual a 19.
if int(hour) >= 19:
	print ("Es hora de irse a casa")
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hour), 59-int(minutes)))