from os import name

import pytest

def calcular_taboada(numero, multiplicador):


 for numero in range(0, 11):
    print(f'{numero} * {multiplicador} = {numero * multiplicador}')


def calcular_fosforos(num1, num2):
 return num1 * num2


def testar_fosforos():

 num1 = 40
 num2 = 5
 resultado_esperado = 200
 resultado_atual = calcular_fosforos(num1, num2)
 assert resultado_esperado == resultado_atual


def testar_calcular_taboada():


    numero = 2
    multiplicador = 3
    resultado_esperado = None
    resultado_atual = calcular_taboada(numero,multiplicador)
    assert resultado_esperado == resultado_atual


