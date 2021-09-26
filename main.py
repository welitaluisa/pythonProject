# imports - bibliotecas

#TDD : Desenvolvimento Direcionado pelo Testes
# - Criar o esqueleto de classes, funções e métodos logo no início da Sprint
# - Criar pelo 1 teste (feliz) para todas as funções e métodos
# - Executar todos os testes unitários diariamente para medir o progresso

import pytest


# 2 - class - classes

# 3 - definitions - definições = métodos e funções

def print_hi(name):
    print(f'Oi, {name}') # a partir do python 3
    print('oi, ' + name) # antes do python 3

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2


def dividir(num1, num2):
    if num1 != 0:
        return num1 / num2
    else:
        return "Não dividir número igual a 0"

def multiplicar(num1, num2):
    return num1 * num2

def calcular_area_do_retangulo(largura, comprimento):
        return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado**2

def calcular_area_do_triangulo(largura, comprimento):
    return largura*comprimento/2

# testes unitários / Testes de UNidades

# testes da função somar
def test_somar():
    # 1 - Configura / Prepara
    num1 = 8  # input / entrada
    num2 = 5  # input / entrada
    resultado_esperado = 13  # output / saida
     # 2 - Executa
    resultado_atual = somar(num1, num2)

    # 3 - Check / Valida
    assert resultado_atual == resultado_esperado


# o mesmo teste só que resumido
def test_somar_compacto():
    assert somar(8, 5) == 13


def test_somar_resultado_negativo():
    assert somar(-1000, -2000) == -3000

def test_subtrair():
    assert somar(4, 5) == 9


def teste_multiplicar():
    assert multiplicar(3, 7) == 21

def teste_dividir():
    assert dividir(3, 7) == 0.42857142857142855

def teste_calcular_area_do_retangulo():
    assert calcular_area_do_retangulo(5,7) == 35

def teste_calcular_area_do_quadrado():
    assert calcular_area_do_quadrado(5) == 25

def test_calcular_area_do_triangulo():
    assert calcular_area_do_triangulo(3,4)==6

if __name__ == '__main__':
    print_hi('welita')

    resultado = somar(1, 2)
    print(f'O resultado de somar é: {resultado}')

    resultado = subtrair(14, 23)
    print(f'O resultado de subtrair é: {resultado}')

    resultado = dividir(0, 782)
    print(f'O resultado de dividir é: {resultado}')

    resultado = multiplicar(14, 211)
    print(f'O resultado de multiplicar é: {resultado}')

    resultado = multiplicar(14, 211)
    print(f'O resultado de multiplicar é: {resultado}')










