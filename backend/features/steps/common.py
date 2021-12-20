from behave import *
from ahorcado.ahorcado import Ahorcado

@when('"{text}" ha ingresado su nombre')
def step_impl(context, text):
    context.ahorcado.login(text)

@given('"{text}" ha ingresado su nombre')
def step_impl(context, text):
    context.ahorcado.login(text)

@given('la palabra a adivinar es "{text}"')
def step_impl(context, text):
    context.ahorcado.set_palabra(text)

@given('"{text}" ingresa su nombre')
def step_impl(context, text):
    context.ahorcado.login(text)
