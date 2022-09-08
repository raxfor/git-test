class Alumno:
    def __init__(self, nombre, nota) :
        self.Nombre = nombre
        self.Nota = nota

    def aprobado(self):
        if self.Nota >= 3 and self.Nota <= 5:
            return "aprobado"
        else:
            return "No aprobo"

alex = Alumno("Edwin alexander", 2)
print("El estudiante", alex.Nombre , "con una nota de", alex.Nota,alex.aprobado())
