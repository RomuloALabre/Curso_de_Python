'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta
'''
matriz = [[], [], [], [], [], [], [], [], []]
num = 0
for c in range(0, 9):
    num = int(input(f'{c+1}º número da matriz: '))
    matriz[c].append(num)
for m in range(0, 3):
    print(matriz[m], end='')
print()
for n in range(3, 6):
    print(matriz[n], end='')
print()
for o in range(6, 9):
    print(matriz[o], end='')