from behave import *
from ahorcado.ahorcado import Ahorcado

@given('se ha inicializado una partida con palabra a adivinar "{text}"')
def step_impl(context, text):
    ahorcado = Ahorcado()
    ahorcado.set_palabra(text)
    context.ahorcado = ahorcado

@when('el jugador arriesga la palabra "{text}"')
def step_impl(context, text):
    context.ahorcado.arriesgar_una_palabra(text)

@then('habrá ganado la partida')
def step_impl(context):
    assert context.ahorcado.get_codigo_estado() == 1
