'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
from random import randint
sorteio = (randint(1  , 10), randint(1  , 10), randint(1  , 10), randint(1  , 10), randint(1  , 10))
print(f'Os valores sorteados foram: ', end='')
for s in sorteio:
    print(f'{s} ',end='')
print(f'\nO menor número é: {sorted(sorteio)[0]}')
print(f'O maior número é: {max(sorteio)}')