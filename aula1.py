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
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIN!')
        else:
            print('{:0>3}'.format(numero))

def exibir_dia_da_semana_if(numero):
    print('Execução com IF')
    if   numero == 1:
        print('o dia é segunda')
    elif numero == 2:
        print('o dia é terça')
    elif numero == 3:
        print('o dia é quarta')
    elif numero == 4:
        print('o dia é quinta')
    elif numero == 5:
        print('o dia é sexta')
    elif numero == 6:
        print('o dia é sabado')
    elif numero == 7:
        print('o dia é domingo')
    else:
        print('Numero de dia invalido. Digite um número de 1 a 7')
'''
def exibir_dia_da_semana_match(numero):
    print('Execução com MATCH')
    match numero:
        case 1:
            print('o dia é segunda')
            exit();
        case 2:
            print('o dia é terça')
            exit();
        case 3:
            print('o dia é quarta')
            exit();
        case 4:
            print('o dia é quinta')
            exit();
        case 5:
            print('o dia é sexta')
            exit();
        case 6:
            print('o dia é sabado')
            exit();
        case 7:
            print('o dia é domingo')
            exit();
        case _:
            print('Numero de dia invalido. Digite um número de 1 a 7')

'''
def brincar_de_parar_ou_continuar():
    resposta = 'C' # C aqui significa que continua

    while resposta.upper() =='C':
        resposta = input("Digite C parar continuar ou qualquer outra letra para parar")
    print('Você decidiu parar com a brincadeira')

 # chamar a função de calculo a área do  retangulo

if __name__ == '__main__':
    print_hi('welita')

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

# exemplo de dia da semana com if - elif - else

exibir_dia_da_semana_if('')

#exemplo de dia da semana com match - case
#exibir_dia_da_semana_match(1)

#exemplo com while - parar ou continuar
brincar_de_parar_ou_continuar()
