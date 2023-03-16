#   Exercício Python 060 - Cálculo do Fatorial
#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
#   Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''
from math import factorial
num = int(input('Digite um número: '))
fatorial = factorial(num)
print(f'O fatorial de {num} é {fatorial}')
'''
num = int(input('Digite um número: '))
f = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
for f in range(num , 0, -1):
    fatorial *= f
    print(f'{f}', end='')
    print(' x 'if f > 1 else ' = ', end='')
    f -= 1 
print(fatorial)