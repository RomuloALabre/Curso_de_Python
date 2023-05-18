"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randrange
def maior():
    r = maior = 0
    while True:
        print('-='*20)
        if r == 0:
            r = maior
        print(f'Os numeros sorteados foram: ',end='')
        for i in range(0 , 5):
            r = randrange(1 , 10)
            print(f'{r}, ' ,end='')
            i += 1
            if r > maior:
                maior = r
        print(f'\nO maior entre eles é o numero {maior}')
        print('-='*20)
        break
#Programa principal
maior()