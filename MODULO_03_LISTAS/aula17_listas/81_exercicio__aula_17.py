'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é: {lista}')
if 5 not in lista:
    print('O valor "5" não está na lista')
else:
    print('Temos o valor "5" na lista')