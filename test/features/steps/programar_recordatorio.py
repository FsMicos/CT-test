import sys
import os
from behave import *
from src.GestorRecordatorio import GestorRecordatorio
from src.Estudiante import Estudiante
from src.Libro import Libro
from src.Acuerdo import Acuerdo

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


@step("se genera un recordatorio para ese intercambio faltando (?P<dias_restantes>.+) con un nivel de urgencia (?P<nivel_urgencia>.+)")
def step_impl(context, dias_restantes, nivel_urgencia):
    dias_restantes = int(dias_restantes)
    nivel_urgencia = nivel_urgencia.upper()
    acuerdo = context.acuerdo
    gestor = GestorRecordatorio()
    recordatorio = gestor.generar_recordatorio(acuerdo, dias_restantes)
    assert recordatorio['nivel_urgencia'] == nivel_urgencia, (
        f"Nivel de urgencia esperado: {nivel_urgencia}, pero se generó: {recordatorio['nivel_urgencia']}"
    )

    for estudiante in acuerdo.estudiantes:
        estudiante.agregar_recordatorio(recordatorio)

    context.mensaje_generado = recordatorio['mensaje']

@step("se agrega la notificación de recordatorio para ambos estudiantes con el mensaje (?P<mensaje>.+)")
def step_impl(context, mensaje):
    acuerdo = context.acuerdo
    estudiantes = acuerdo.estudiantes

    for estudiante in estudiantes:
        mensajes_encontrados = [r['mensaje'] for r in estudiante.recordatorios if r['mensaje'] == mensaje]
        assert mensajes_encontrados, (
            f"No se encontró el mensaje esperado en los recordatorios de {estudiante.nombre}.\n"
            f"Mensajes encontrados: {[r['mensaje'] for r in estudiante.recordatorios]}"
        )