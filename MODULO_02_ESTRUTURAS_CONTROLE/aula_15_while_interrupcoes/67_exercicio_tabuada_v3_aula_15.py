"""
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
tabuada = 0
while True:
    n = int(input('Digite a tabuada que deseja: '))
    print('-' * 10)
    if n < 0:
        break
    c = 1
    for c in range(1, 11):
        tabuada = n * c
        print(f'{n} x {c} = {tabuada}')
        c += 1
    print('-' * 10)
print('Programa interrompido. Volte sempre!')