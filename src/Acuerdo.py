from enum import Enum

from src.Libro import Libro

class Acuerdo:
    def __init__(self, libro_1: Libro,libro_2: Libro):
        self.libro_1 = libro_1
        self.libro_2 = libro_2
        self.confirmadoE1 = False
        self.confirmadoE2 = False
        self.dias_restantes = 0
        self.Estado = EstadosAcuerdo.PENDIENTE
    def setDiasRestantes(self, dias_restantes):
        self.dias_restantes = dias_restantes

    def getEstado(self):
        return self.Estado

class EstadosAcuerdo(Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"