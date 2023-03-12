'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for pes in range(1, 8):
    nasc = int(input(f'Insira ano de nascmento da {pes}º pessoa: '))
    idade = atual - nasc
    if idade < 18:
        print(f'Ainda não atingiu a maior idade. Tem {idade} anos')
        menor += 1
    else:
        print(f'Atingiu maior idade. É um adulto de {idade} anos.')
        maior += 1
print(f'Pessoas com menor idade: {menor}')
print(f'Pessoas com maior idade: {maior}')





