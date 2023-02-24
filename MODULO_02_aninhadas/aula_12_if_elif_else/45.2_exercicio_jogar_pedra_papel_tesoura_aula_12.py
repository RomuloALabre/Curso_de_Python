'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('Digite sua jogada: \n 1 = PEDRA\n 2 = PAPEL ou \n 3 = TESOURA')
jogador = int(input('Vamos lá, qual é a sua JOGADA? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.5)
print('-=' * 15)
print(f'Computador escolheu: {itens[computador]}')
print(f'Você jogou: {itens[jogador]}')
print('-='* 15)

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida, JOGUE NOVAMENTE!')

elif computador == 1: #PAPEL
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!!!')
    elif jogador == 0:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida, JOGUE NOVAMENTE!')

elif computador == 2: #TESOURA
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('VOCÊ VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida, JOGUE NOVAMENTE!')