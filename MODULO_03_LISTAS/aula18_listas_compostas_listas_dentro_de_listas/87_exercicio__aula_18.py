'''
Aprimore o desafio anterior, mostrando no final:
a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
coluna3 = []
maior = soma = somac = 0
for l in range(0, 3):
    for c in range(0, 3): 
        matriz[l][c] = int(input(f'Digite valor da posição [{l}][{c}]: '))
        #num = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
            soma = soma + matriz[l][c]
        if c == 2:
            coluna3.append(matriz[l][c])
            somac = somac + matriz[l][c]
        if l == 1:
            if maior == 0:
                maior = matriz[l][c]
            elif maior <= matriz[l][c]:
                maior = matriz[l][c]
print('A matriz gerada foi: ')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
pares.sort()
print(f'Os números pares que compõem essa MATRIZ são: {pares} cuja soma é: {soma}')
print(f'Os valores da 3º coluna são: {coluna3} cuja soma é: {somac}')
'''OU SEM CRIAR A LISTA COLUNA3'''
print(f'OU buscando direto na matriz: {matriz[0][2]}, {matriz[1][2]}, {matriz[2][2]}')
print(f'O maior número da 2º linha é: {maior}')