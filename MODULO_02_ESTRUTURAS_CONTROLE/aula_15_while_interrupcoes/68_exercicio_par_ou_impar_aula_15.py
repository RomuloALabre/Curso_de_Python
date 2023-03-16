"""
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep
v = 0
print('Vamos bricar de PAR ou IMPAR !?')
while True:
    u = str(input('Você escolhe PAR ou IMPAR: ')).upper().strip()
    n = int(input('Digite o seu número: '))
    c = randint(0 , 10)
    print('DO LÁ CI... ')
    sleep(2)
    print('JÁ!!!\n---')
    sleep(0.5)
    if (n + c) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'  
    print(f'Você jogou: {n}')
    print(f'PC jogou: {c}\n---')
    print(f'O resultado deu: {result}')
    if u == result:
        print('Você GANHOU!!! Continue jogando...\n---')
        v += 1
        sleep(1)
    else:
        print('Essa você perdeu!\n---')
        break
print(f'Total de vitórias: {v}')