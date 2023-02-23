'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
print('Vamos jogar pedra, papel, tesou? ')
print('Digite o número correspondente: \n 1 para escolher pedra\n 2 = papel ou \n 3 = tesoura')
game = int(input('Vamos lá, qual numero você escolhe? '))
sort = randint(1 , 3)
print(sort)
if sort == game:
    print('voce ganhou!!!')
else:
    print('Você perdeu.')