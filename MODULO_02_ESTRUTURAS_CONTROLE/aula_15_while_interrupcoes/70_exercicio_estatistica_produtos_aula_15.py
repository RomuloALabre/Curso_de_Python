"""
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
total = caro = barato = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    if preco < barato or barato == 0:
        barato = preco
        pbarato = produto
    if preco > 1000:
        caro += 1
    total += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais produtos S/N? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'\nFIM DO PROGRAMA\nTotal gasto: R$ {total:.2f}')
print(f'Produto com preço maior que R$ 1000,00: {caro}')
print(f'O produto mais barato é {pbarato}, custando R$ {barato:.2f}')