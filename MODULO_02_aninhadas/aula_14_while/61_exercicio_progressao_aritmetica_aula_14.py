#   Exercício Python 061 - Progressão Aritmética v2.0
#   Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#   mostrando os 10 primeiros termos da progressão usando a estrutura while.
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
d = int(input('Quantos termos deseja: '))
c = 0
pa = 0
while c != d:
    pa += r
    c += 1
    print(f'O {c}º termo da PA é: {pa}')