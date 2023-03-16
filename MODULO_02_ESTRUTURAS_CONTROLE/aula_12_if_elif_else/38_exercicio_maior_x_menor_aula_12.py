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
    print(f'O número {numa:.0f} é maior que {numb:.0f}')
elif numb > numa:
    print(f'O número {numb:.0f} é maior que {numa:.0f}')
else:
    print('Os números são iguais!')