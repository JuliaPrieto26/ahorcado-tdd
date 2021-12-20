from behave import *
from ahorcado.ahorcado import Ahorcado
import features.steps.login
import features.steps.common

@given('hemos inicializado una partida')
def step_impl(context):
    context.ahorcado = Ahorcado()

@then('podre ver que su nombre es "{text}"')
def step_impl(context, text):
    nombre_guardado = context.ahorcado.get_nombre()
    assert nombre_guardado == text
