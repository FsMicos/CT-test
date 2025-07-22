class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.recordatorios = []
    def agregar_recordatorio(self, recordatorio):
        self.recordatorios.append(recordatorio)
