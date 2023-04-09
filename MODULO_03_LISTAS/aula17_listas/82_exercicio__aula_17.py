'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
ímpar = []
par = []
while True:
    lista.append(int(input('Digite um número para listar: ')))
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
for l in lista: #OU for i, l in enumerate(lista):
    if l % 2 == 0:
        par.append(l)
    else:
        ímpar.append(l)
print(f'\nA lista digitada foi {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {ímpar}\n')