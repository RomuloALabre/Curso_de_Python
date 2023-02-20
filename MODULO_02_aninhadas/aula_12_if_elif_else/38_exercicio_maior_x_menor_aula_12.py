'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
numa = float(input('Digite um número: '))
numb = float(input('Digite o segundo número: '))
if numa > numb:
    print(f'O número {numa} é o maior')
elif numb > numa:
    print(f'O número {numb} é o maior')
else:
    print('Os números são iguais!')