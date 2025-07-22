import sys
import os
from behave import *
from src import GestorRecordatorio
from src.Estudiante import Estudiante
from src.Libro import Libro
from src.Acuerdo import Acuerdo
from src.Recordatorio import Recordatorio, NivelUrgencia

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

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

    # Verificar que se crearon exactamente 2 estudiantes
    assert len(nombres_estudiantes) == 2, f"Se esperaban 2 estudiantes, pero se crearon {len(nombres_estudiantes)}"

    primer_estudiante = nombres_estudiantes[0]
    segundo_estudiante = nombres_estudiantes[1]
    libro_1 = context.libros[primer_estudiante]
    libro_2 = context.libros[segundo_estudiante]

    # Verificar que los libros tienen diferentes dueños
    assert libro_1.dueño != libro_2.dueño, "Los libros deben pertenecer a estudiantes diferentes"

    context.acuerdo = Acuerdo(libro_1=libro_1, libro_2=libro_2)


@step("que el acuerdo tiene estado pendiente")
def step_impl(context):
    # Verificar que el acuerdo existe y tiene el estado correcto
    assert hasattr(context, 'acuerdo'), "No se ha creado un acuerdo previamente"
    assert context.acuerdo.getEstado() == "Pendiente", f"El estado del acuerdo debería ser 'Pendiente' pero es '{context.acuerdo.getEstado()}'"

    # Verificar que las confirmaciones están en false (lógica de negocio)
    assert context.acuerdo.confirmadoE1 == False, "El estudiante 1 no debería haber confirmado en un acuerdo pendiente"
    assert context.acuerdo.confirmadoE2 == False, "El estudiante 2 no debería haber confirmado en un acuerdo pendiente"

@step("que faltan (?P<dias_restantes>.+) días para la fecha del intercambio")
def step_impl(context, dias_restantes):
    dias_restantes = int(dias_restantes)

    # Verificar que los días restantes sean válidos (lógica de negocio)
    assert dias_restantes >= 0, f"Los días restantes no pueden ser negativos: {dias_restantes}"

    context.acuerdo.setDiasRestantes(dias_restantes)

    # Verificar que se asignó correctamente
    assert context.acuerdo.dias_restantes == dias_restantes, f"Los días restantes no se asignaron correctamente. Esperado: {dias_restantes}, Actual: {context.acuerdo.dias_restantes}"


@step("se genera un recordatorio para ese intercambio")
def step_impl(context):
    # Verificar que existe un acuerdo antes de generar el recordatorio
    assert hasattr(context, 'acuerdo'), "No se puede generar un recordatorio sin un acuerdo previo"
    assert context.acuerdo.dias_restantes >= 0, "No se puede generar recordatorio con días restantes inválidos"

    context.recordatorio = GestorRecordatorio.gestionar_recordatorio(context.acuerdo)

    # Verificar que se creó el recordatorio correctamente
    assert context.recordatorio is not None, "No se pudo generar el recordatorio"
    assert isinstance(context.recordatorio, Recordatorio), "El objeto generado no es un Recordatorio válido"
    assert context.recordatorio.acuerdo == context.acuerdo, "El recordatorio no está asociado al acuerdo correcto"


@step("el recordatorio debe tener un nivel de urgencia (?P<nivel_urgencia>.+)")
def step_impl(context, nivel_urgencia):
    # Verificar que existe el recordatorio
    assert hasattr(context, 'recordatorio'), "No se ha generado un recordatorio previo"
    assert context.recordatorio is not None, "El recordatorio no puede ser None"

    # Verificar que el nivel de urgencia es válido
    niveles_validos = [nivel.value for nivel in NivelUrgencia]
    assert nivel_urgencia in niveles_validos, f"Nivel de urgencia '{nivel_urgencia}' no es válido. Niveles válidos: {niveles_validos}"

    # Verificar que el nivel de urgencia del recordatorio coincide con lo esperado
    assert context.recordatorio.nivel_urgencia == nivel_urgencia, f"Nivel de urgencia incorrecto. Esperado: '{nivel_urgencia}', Actual: '{context.recordatorio.nivel_urgencia}'"

    # Verificar la lógica de negocio según los días restantes
    dias_restantes = context.acuerdo.dias_restantes
    if dias_restantes >= 5:
        assert nivel_urgencia == "BAJO", f"Con {dias_restantes} días restantes, el nivel debería ser BAJO"
    elif dias_restantes >= 3:
        assert nivel_urgencia == "MEDIO", f"Con {dias_restantes} días restantes, el nivel debería ser MEDIO"
    else:
        assert nivel_urgencia == "ALTO", f"Con {dias_restantes} días restantes, el nivel debería ser ALTO"
