# Faça um programa que leia um ano qualquer e mostre se ele é ano bissexto.
from datetime import date
ano = int(input('Insira o ano: '))
if ano == 0:
    # 0 equivale ao ano atual, que será buscado no sistema do computador
    ano = date.today().year
if ano % 4 == 0 and ano %100 !=  0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')