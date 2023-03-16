#   Exercício Python 063 - Fibonacci
#   Escreva um programa que leia um número N inteiro qualquer e mostre na tela
#   os N primeiros elementos de uma Sequência de Fibonacci.
n1 = 0
n2 = 1
element = int(input('Quantos elementos? '))
c = 0
f = 0
print(f'{n1} - ', end='')
print(f'{n2} - ', end='')
while c < element - 2:
    f = n1 + n2
    print(f'{f} - ', end='' )
    n1 = n2
    n2 = f
    c += 1
print('Terminou')