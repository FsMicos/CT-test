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
  Y que faltan <dias_restantes> días para la fecha del intercambio
  Cuando se genera un recordatorio para ese intercambio
  Entonces el recordatorio debe tener un nivel de urgencia <nivel_urgencia>
  Ejemplos:
    |dias_restantes|nivel_urgencia|
    |5             |BAJO|
    |3          | MEDIO|
    |2          | ALTO|
