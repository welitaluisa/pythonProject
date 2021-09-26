# 1 - IMPORTS/ BIBLIOTECAS

import pytest


# 2 - MÉTODOS E FUNÇÕES
# 3 - CLASSES

# DEF = DEFINITION = DEFINIÇÃO


def print_hi(name):
    print(f'Oi, {name}') # a partir do python 3
    print('oi, ' + name) # antes do python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_triangulo(largura, comprimento):

    return largura * comprimento / 2


def contagem_progressiva(fim):
    for numero in range(fim):  # repete o bloco de zero ate o fim
        print(numero)  # exibe o número


def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print( f'{contador} - {nome}')

        if numero < 9:
            print(f'00 -', numero + 1, '-', nome)
        elif numero < 99:
            print(f'0 -', numero + 1, '-', nome)
        else:
            print(numero + 1, ' -  ', nome)

def brincar_de_plim(fim):
    for numero in range (fim):
        if numero % 4 == 0:
            print('PLIN!')
        else:
            print('{:0>3}'.format(numero))


 # chamar a função de calculo a área do  retangulo

resultado = calcular_area_do_retangulo(3, 4)
print(f'A área do retangulo é de {resultado} m²')

# chamar a função de calculo do quadrado

resultado = calcular_area_do_quadrado(5)
print(f'A área do quadrado é de {resultado} m²')

# chamar a função de calculo do triangulo

resultado = calcular_area_do_triangulo(3, 4)
print(f'A área do triangulo é de {resultado} m²')

# executar uma chamada regressiva

contagem_progressiva(11)

# exibir o nome do canditado varias vezes
apoiar_candidato('Faker', 100)

# Brincar de Plim
brincar_de_plim(100)