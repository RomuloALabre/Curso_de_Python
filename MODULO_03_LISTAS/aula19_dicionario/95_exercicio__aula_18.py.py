"""
 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. 
 Depois vai ler a quantidade de gols feitos em cada partida. 
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
 (No final mostrar um resumo da temporada do jogador e o total de gols)
""""""
 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()
partidas = list()
times = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input(f'Nome: '))
    tot = int(input(f'Nº de partidas que {jogador["nome"]} jogou? '))
    for c in range (0 , tot):
        partidas.append(int(input(f'   Nº de gols na {c} partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    
    while True:
        resp = str(input('Cadastrar mais jogadores? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas SIM ou NÃO.')
    if resp == 'N':
        print('Cadastro Finalizado!')
        break
print('-='*30)
print('cod. ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(times):
    print(f'{k+1:>2}', end=' ')
    for i in v.values():
        print(f'{str(i):<15}',end='  ')
    print()
print('-='*30)
while True:
    busca = int(input('Digite o código do jogador que deseja filtrar: (0 para sair)'))
    if busca == 0:
        print(' -- Programa Encerrado -- ')
        break
    if busca > len(times):
        print(f'Código {busca} inválido!')  
    else:
        busca-=1
        print(f' -- Buscando Jogador... {times[busca]["nome"]}')
        for i, g in enumerate(times[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
