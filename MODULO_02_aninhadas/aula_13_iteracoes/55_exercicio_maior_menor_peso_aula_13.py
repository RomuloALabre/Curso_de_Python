'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso lido.'''
menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso            
        if peso > maior:
            maior = peso
print(f'O Menor peso é: {menor:.0f} Kg')
print(f'O Maior peso é: {maior:.0f} Kg')