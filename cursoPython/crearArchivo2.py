from pickle import *

# The class Vehiculo has two attributes, modelo and velocidad, and one method, __str__.
class Vehiculo:

    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    def __str__(self):
        return self.modelo + " " + self.velocidad


# Creating an object of the class Vehiculo and printing it.
bmw = Vehiculo("2020", "180km/h")
print(bmw)

# Opening a file called automovil in write and binary mode.
file = open('automovil', 'w+b')

# Writing the object bmw into the file.
dump(bmw, file)

# Loading the object from the file.
file.seek(0)
newBmw = load(file)

print(newBmw)
file.close()