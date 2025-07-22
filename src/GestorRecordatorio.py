
class GestorRecordatorio:

    def generar_recordatorio(self, acuerdo, dias_restantes):
        nivel_urgencia = self.calcular_nivel_urgencia(dias_restantes)
        mensaje = f"Recordatorio: Faltan {dias_restantes} días para confirmar tu intercambio. Urgencia: {nivel_urgencia.upper()}."
        recordatorio = {
            'acuerdo': acuerdo,
            'dias_restantes': dias_restantes,
            'nivel_urgencia': nivel_urgencia.upper(),
            'mensaje': mensaje
        }
        return recordatorio

    def calcular_nivel_urgencia(self, dias_restantes):
        if dias_restantes <= 1:
            return "ALTO"
        elif dias_restantes <= 3:
            return "MEDIO"
        else:
            return "BAJO"