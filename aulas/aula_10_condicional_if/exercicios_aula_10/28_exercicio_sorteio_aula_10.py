#Escreva um programa que faça um computador pensar em um numero entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

sorteio = random.randint(0,5)
num = int(input('Escolha um numero de 0 a 5: '))

if num > 5:
    print('Número inválido!')
    num = int(input('Escolha um numero de 0 a 5: '))
if num == sorteio:
    print('Você ganhou!')
else:
    print('Você perdeu!')
print(f'Número sorteado: {sorteio}')
print(f'Número escolhido: {num}')
