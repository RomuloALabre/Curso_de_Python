"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randrange
def sorteia(lista):
    print('-='*25)
    for n in range(0 , 5):
        numeros.append(randrange(1 , 10))
    print(f'Os números sorteados foram: ', end='')
    print(numeros)

def somaPar(lista):
    soma = 0
    print('-='*25)
    print(f'Os números pares foram: ', end='')
    for i in numeros:
        if i % 2 == 0:
            print(f'{i} ', end='')
            soma += i
    print(f'\nA soma é: {soma}')
    print('-='*25)

#Programa principal
numeros = list()
sorteia(numeros)
somaPar(numeros)