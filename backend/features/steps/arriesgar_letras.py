from behave import *
from ahorcado.ahorcado import Ahorcado
import features.steps.login

@when('el usuario arriesga la letra "{letra}"')
def step_impl(context, letra):
    context.ahorcado.arriesgar_una_letra(letra)

@then('el usuario habrá acertado una letra y tendrá cero errores')
def step_impl(context):
    assert context.ahorcado.get_aciertos_errores() == (1, 0)

@then('el usuario habrá errado una letra y tendrá un error')
def step_impl(context):
    assert context.ahorcado.get_aciertos_errores() == (0, 1)

@then('el usuario habrá acertado tres veces y tendrá cero errores')
def step_impl(context):
    assert context.ahorcado.get_aciertos_errores() == (3, 0)
