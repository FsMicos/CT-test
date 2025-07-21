from behave import *
from src.Estudiante import Estudiante
from src.Libro import Libro
from src.Acuerdo import Acuerdo

use_step_matcher("re")


@step("que dos estudiantes han acordado un intercambio")
def step_impl(context):
    context.estudiantes = {}
    context.libros = {}
    nombres_estudiantes = []
    for row in context.table:
        nombre_estudiante = row["nombre"]
        nombre_libro = row["libro"]
        context.estudiantes[nombre_estudiante] = Estudiante(nombre=nombre_estudiante)
        context.libros[nombre_estudiante] = Libro(
            nombre=nombre_libro,
            estudiante=context.estudiantes[nombre_estudiante]
        )
        nombres_estudiantes.append(nombre_estudiante)
    primer_estudiante = nombres_estudiantes[0]
    segundo_estudiante = nombres_estudiantes[1]
    libro_1 = context.libros[primer_estudiante]
    libro_2 = context.libros[segundo_estudiante]
    context.acuerdo = Acuerdo(libro_1=libro_1, libro_2=libro_2)


@step("que el acuerdo tiene estado pendiente")
def step_impl(context):
    # no se si sea necesario verificar esto, debido a que en cuando se crea el acuerdo, este ya se encuentra pendiente
    #respuestas, vi un escenario en el que se verifica un estado que fue modificado o seteado en un step anterior:
    # dado que corto la pizza en 6 trozos, cuando me coma 5 trozos, entonces deberia tener 1 restante.
    assert context.acuerdo.getEstado() == "Pendiente"

@step("que faltan (?P<dias_restantes>.+) días para la fecha del intercambio")
def step_impl(context, dias_restantes):
    dias_restantes =int(dias_restantes)
    context.acuerdo.setDiasRestantes(dias_restantes)


@step("se genera un recordatorio para ese intercambio")
def step_impl(context):
    context.recordatorio = GestorRecordatorio.gestionar_recordatorio(context.acuerdo)


@step("el recordatorio debe tener un nivel de urgencia (?P<nivel_urgencia>.+)")
def step_impl(context, nivel_urgencia):

    assert context.recordatorio.nivel_urgencia == nivel_urgencia