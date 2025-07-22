from src.Recordatorio import Recordatorio, NivelUrgencia
from src.Acuerdo import Acuerdo

def gestionar_recordatorio(acuerdo: Acuerdo):
    """
    Genera un recordatorio basado en los días restantes para el intercambio
    - 5+ días: nivel BAJO
    - 3-4 días: nivel MEDIO
    - 1-2 días: nivel ALTO
    """
    dias_restantes = acuerdo.dias_restantes

    if dias_restantes >= 5:
        nivel = NivelUrgencia.BAJO.value
    elif dias_restantes >= 3:
        nivel = NivelUrgencia.MEDIO.value
    else:
        nivel = NivelUrgencia.ALTO.value

    return Recordatorio(acuerdo, nivel)
