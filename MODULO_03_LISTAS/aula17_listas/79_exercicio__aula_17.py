'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
numeros = list()
num = 0
while True:
    num = int(input(f'Digite um número: '))
    if num in numeros:
        print('O numero ja existe')
    else:
        numeros.append(num)
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        numeros.sort()
        print(f'A lista é: {numeros}')
        break