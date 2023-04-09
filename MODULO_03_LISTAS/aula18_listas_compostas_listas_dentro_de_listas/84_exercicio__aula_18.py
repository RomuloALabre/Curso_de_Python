'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:
a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com o mais leve e o mais pesado. Se houver mais de um com esse peso, insere na lista.
'''
pessoas = list()
dados = list()
leve = pesada = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso em Kg: ')))
    if len(pessoas) == 0:
        leve = pesada = dados[1]
    else:
        if dados[1] < leve:
            leve = dados[1]
        if dados[1] > pesada:
            pesada = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(f'\nForam cadastradas {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] == leve:
        print(f'O Mais leve foi {p[0]} com {leve} Kg')
    if p[1] == pesada:
        print(f'O mais pesado foi {p[0]} com {pesada} Kg')