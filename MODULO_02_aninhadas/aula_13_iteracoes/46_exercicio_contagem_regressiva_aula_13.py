'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
print('\nATENÇÃO PARA A CONTAGEM REGRESSIVA...\n')
for f in range (10, -1, -1):
    sleep(1)
    print(f)   
print('\nBUM, BUM, POW!!!')
print('PARABÉNSSSSSSSSS VOCÊ VENCEU!!!\n')
