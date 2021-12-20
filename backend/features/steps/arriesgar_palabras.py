from behave import *
from ahorcado.ahorcado import Ahorcado
import features.steps.login
import features.steps.common

@when('el usuario arriesga la palabra "{text}"')
def step_impl(context, text):
    context.ahorcado.arriesgar_una_palabra(text)

@then('el usuario habrá perdido la partida')
def step_impl(context):
    assert context.ahorcado.get_codigo_estado() == -1

@then('el usuario habrá ganado la partida')
def step_impl(context):
    assert context.ahorcado.get_codigo_estado() == 1
