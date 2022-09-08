class Vehiculo:
    def __init__(self, color, ruedas, puertas) :
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas



class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.Velocidad = velocidad
        self.Cilindrada = cilindrada


spark = Coche("azul", 4, 4, "120km/h", "3500cc")
print("SPARK")
print("Color : " ,spark.Color)
print("Ruedas: " ,spark.Ruedas)
print("Puertas: " ,spark.Puertas)
print("Velocidad: " ,spark.Velocidad)
print("Cilindrada: " ,spark.Cilindrada)



