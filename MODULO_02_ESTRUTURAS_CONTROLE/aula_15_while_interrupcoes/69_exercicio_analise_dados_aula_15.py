"""
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
sm = sf = 0
i = imulher = 0
print('Ficha de Cadastro\n---')
while True:
    nome = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo F/M: ')).upper().strip()[0]
    if sexo == 'M':
        sm += 1
    else:
        sf += 1
    idade = int(input('Idade: '))
    if idade >= 18:
        i += 1
    if idade < 20 and sexo == 'F':
        imulher += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja cadastrar mais pessoas? S/N: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Pessoas maiores de 18 anos: {i}')
print(f'Mulheres com menos de 20 anos: {imulher}')
print(f'Homens cadastrados: {sm}')