# Created by Micos at 17/06/2025
# language: es
#capabilitie: programar recordatorio

Característica: Recordatorio automatizado
  Como estudiante universitario
  Quiero recibir recordatorios automáticos sobre mis intercambios acordados
  Para no olvidar concretar los acuerdos
  y evitar intercambios fallidos


 #clases identificadas : estudiante, recordatorio, libro, acuerdo
Esquema del escenario:  Recordatorio de intercambio sin confirmar
  Dado que dos estudiantes han acordado un intercambio
    |nombre | libro |
    |Juana  | El poder del ahora|
    |Pedro  | El camino|
  Y que el acuerdo tiene estado pendiente
  Cuando se genera un recordatorio para ese intercambio faltando <dias_restantes> con un nivel de urgencia <nivel_urgencia>
  Entonces se agrega la notificación de recordatorio para ambos estudiantes con el mensaje <mensaje>
  Ejemplos:
    |dias_restantes|nivel_urgencia| mensaje|
    |5             |BAJO| Recordatorio: Faltan 5 días para confirmar tu intercambio. Urgencia: BAJO.|
    |3          | MEDIO|Recordatorio: Faltan 3 días para confirmar tu intercambio. Urgencia: MEDIO. |
    |1          | ALTO| Recordatorio: Faltan 1 días para confirmar tu intercambio. Urgencia: ALTO.  |
