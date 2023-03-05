'''Refaça o DESAFIO 009 ( faça a tabuada de um numero escolhido pelo usuario), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
n = int(input('Insira a tabuada que você deseja: '))
print(f'A tabuada de {n} é: ')
for c in range(0 , 11):
    tabuada = n * c
    print(f'{n} x {c} = {tabuada}')

    