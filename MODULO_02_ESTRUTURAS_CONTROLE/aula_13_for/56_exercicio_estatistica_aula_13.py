'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homen mais velho.
Quantas mulheres têm menos de 20 anos.'''
mulhernova = 0
homem = ''
velho = 0
soma = 0
for p in range(1 , 5):
    print(f'=== {p}º PESSOA ===')
    nome = str(input('Nome: ')).strip()
    sexo = str(input('O sexo (F/M): ')).strip().lower()
    idade = int(input('Idade: '))
    soma += idade 
    if p == 1 and sexo == 'm':
            velho = idade
            homem = nome
    else:
        if sexo == 'm' and idade > velho:
                velho = idade
                homem = nome
        if sexo == 'f' and idade < 20:
                mulhernova += 1
media = soma / 4
print(f'{homem} é o homem mais velho, com {velho} anos')
print(f'Tem {mulhernova} mulher(s) com menos de 20 anos.')
print(f'E a média de idade dessa família é: {media:.2f} anos.')