from src.Estudiante import Estudiante
class Libro:
    def __init__(self, nombre, estudiante: Estudiante):
        self.nombre = nombre
        self.dueño = estudiante

