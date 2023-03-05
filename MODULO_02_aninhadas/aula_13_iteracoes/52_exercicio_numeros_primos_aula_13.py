'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite o número que deseja descobrir se é um número PRIMO: '))
mult = 0
for c in range(1 , num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print(f'{c}')
if mult == 2:
    print(f'\nO número {num} é um número primo')
else:
    print(f'\nO {num} não é primo')