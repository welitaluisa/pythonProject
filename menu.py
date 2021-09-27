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

def sair():
    print('Obrigado e volte sempre!!')


def exibir_menu(escolha):
    opcao = {
        1: print_hi('welita'),
        2: calcular_area_do_retangulo(8, 9),
        3: calcular_area_do_quadrado(4),
        4: calcular_area_do_triangulo(5, 9),
        5: contagem_progressiva(10),
        6: apoiar_candidato('Domingo', 10),
        7: brincar_de_plim(20),
        8: sair()
    }
    return opcao.get(escolha, 'Opção Inválida')


if __name__ == '__main__':

        continua = True

   # while continua:
        print('##########################################################################')
        print('#                                                                        #')
        print('#              M  E  N  U    D  E   O  P  Ç  Õ  E  S                    # ')
        print('#                                                                        #')
        print('#             1 - OLÁ MUNDO                                              #')
        print('#             2 - ARÉA DO RETÂNGULO                                      #')
        print('#             3 - ARÉA DO QUADRADO                                       #')
        print('#             4 - ARÉA DO TRIÂNGULO                                      #')
        print('#             5 - CONTAGEM PROGRESSIVA                                   #')
        print('#             6 - APOIAR CANDIDATO                                       #')
        print('#             7 - BRINCAR DE PLIM                                        #')
        print('#                                                                        #')
        print('#             Z - SAIR                                                   #')
        print('#                                                                        #')
        print('##########################################################################')


        escolha = input("Escolha sua opção")
        print(f'A sua escolha foi: {escolha}')

