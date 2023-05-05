"""
 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. 
 Depois vai ler a quantidade de gols feitos em cada partida. 
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
 (No final mostrar um resumo da temporada do jogador e o total de gols)
"""
dados = dict()
partidas = list()
dados['nome'] = str(input('Nome: '))
dados['partidas'] = int(input(f'Nº partidas {dados["nome"]} jogou: '))
cont = 1
total = 0
while cont <= dados['partidas']:
    partidas.append(int(input(f'   Nº de gols na {cont} partida: ')))
    cont += 1
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
