from enum import Enum

class Recordatorio:
    def __init__(self, acuerdo, nivel_urgencia):
        self.acuerdo = acuerdo
        self.nivel_urgencia = nivel_urgencia

class NivelUrgencia(Enum):
    BAJO = "BAJO"
    MEDIO = "MEDIO"
    ALTO = "ALTO"
