'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 + r = a2
a2 + r = a3
a3 + r = a4...'''
a = int(input('Digite o TERMO da PA: '))
r = int(input('Digite a RAZÃO da PA: '))
cont = 1
for c in range(0 , 10):
    print(f'O {cont}º termo da PA é: {a}')
    a += r
    cont += 1