"""
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que
 o vencedor tirou o maior número no dado.
 EX:
 Mostrar os valores sorteados
 em seguida mostrar o ranking dos vencedores
"""
from random import randint
from time import sleep
from operator import itemgetter
aposta = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in aposta.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print('-='*18)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(aposta.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.3)
