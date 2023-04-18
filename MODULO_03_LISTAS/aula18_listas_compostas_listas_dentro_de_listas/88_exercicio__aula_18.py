'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep
jogo = []
listajogos = []
total = 1
print('-'*30)
print('      JOGA DA MEGA SENA      ')
print('-'*30)
qtdjogos = int(input('Quantos jogos você quer fazer? '))
while total <= qtdjogos:
    cont = 0
    while True:
        sorteio = randint(1 , 60)
        if sorteio not in jogo:
            jogo.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    total += 1
    jogo.sort()
    listajogos.append(jogo[:])
    jogo.clear()
print('-='*3, f'SORTEANDO {qtdjogos} JOGOS:', '-='*3)
'''for c in range(0 , qtdjogos):
    print(f'{listajogos[c]}')
    sleep(0.5)'''
for i, l in enumerate(listajogos):
    sleep(1)
    print(f'JOGO {i+1}: {listajogos[i]}')
print('-='*5, '< BOA SORTE! >', '-='*5)
