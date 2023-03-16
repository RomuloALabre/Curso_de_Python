'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
print('Vamos jogar pedra, papel, tesoura? ')
print('Digite o número correspondente: \n 1 = para escolher pedra\n 2 = papel ou \n 3 = tesoura')
jogador = int(input('Vamos lá, qual você escolhe? '))
sort = randint(1 , 3)
print('JO\nKEN\nPO!!!')

if jogador == 1:
    print('Você jogou PEDRA')
if sort == 1:
    print('O computador jogou PEDRA')
if jogador == 2:
    print('Você jogou PAPEL')
if sort == 2:
    print('computador jogou PAPEL')
if jogador == 3:
    print('Você jogou TESOURA')
if sort == 3:
    print('Computador jogou TESOURA')

if sort == jogador:
    print('vocês EMPATARAM!!!')
elif jogador == 1 and sort == 3:
        print('Você VENCEU!!!')
elif jogador == 2 and sort == 1:
        print('Você VENCEU!!!')
elif jogador == 3 and sort == 2:
        print('Você VENCEU!!!')
elif jogador == 3 and sort == 1:
        print('Computador  GANHOU!!!')
elif jogador == 1 and sort == 2:
        print('Computador  GANHOU!!!')
elif jogador == 2 and sort == 3:
        print('Computador  GANHOU!!!')