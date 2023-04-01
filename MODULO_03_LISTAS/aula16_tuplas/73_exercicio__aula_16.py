'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''
times = ("Flamengo", "Corinthians", "Palmeiras", "Fluminense", "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo", "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense", "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná", "Atlético-MG")
'''for t, pos in enumerate(times):
    if t == 0:
        print('Os 5 primeiros colocados são: ')
    if t <= 4:
        print(f'{t + 1}º {pos}')
    if t == 16:
        print('\nOs 4 últimos são: ')
    if t > 15:
        print(f'{t + 1}º {pos}')
    if t == 20:
        break
print(f'Os clubes em ordem alfabética: {sorted(times)}')'''

# OU (Professor)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'xxx\nOs 4 últimos são: {times[-4:]}')
print(f'xxx\nLista em ordem alfabética: {sorted(times)}')
print(f'O clube Chapecoense está na {times.index("Chapecoense")+1} posição.')