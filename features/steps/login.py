from behave import given, when, fail
from ahorcado.ahorcado import Ahorcado

@given('hemos inicializado una partida')
def step_impl(context):
    context.ahorcado = Ahorcado()

@when('"{text}" ingresa su nombre')
def step_impl(context, text):
    context.ahorcado.login(text)

@then('podre ver que su nombre es "{text}"')
def step_impl(context, text):
    nombre_guardado = context.ahorcado.get_nombre()
    if text != nombre_guardado:
        fail(f'{text} is not {nombre_guardado}')
