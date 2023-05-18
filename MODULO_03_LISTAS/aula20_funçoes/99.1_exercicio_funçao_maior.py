"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
def maior(*num):
    n = maior = 0
    print('-='*20)
    print(f'Analisando os valores: ',end='')
    for valor in num:
        print(f'{valor}, ', end='', flush=True)
        sleep(0.2)
        if valor > maior:
            maior = valor
        n += 1
    print(f'\nForam informados: {n} valores')
    print(f'O maior foi: {maior}')
    sleep(1)
    
#Programa principal
maior(1, 2, 3, 4)
maior(0, 3, 5)
maior(0)
maior(2, 8, 3, 5)