"""
EXERCÍCIO 066: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
soma = s = 0
c = 1
print('Digite números para somar ou "999" para sair!')
while True:
    n = int(input(f'Digite o {c}º número que deseja somar: '))
    if n == 999:
        print('Você saiu do programa.')
        break
    s += 1
    c += 1
    soma += n
print(f'Você digitou {s} números e a soma é: {soma}')