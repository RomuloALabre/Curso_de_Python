#Crie um programa que leia um número e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Insira um numero: '))
if num % 2:
    print(f'O numero {num} é ÍMPAR')
else:
    print(f'O numero {num} é PAR')