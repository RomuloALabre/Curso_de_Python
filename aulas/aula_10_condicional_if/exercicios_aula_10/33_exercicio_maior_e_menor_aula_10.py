# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
if a > b and a > c:
    print(f'O maior é: {a}')
elif b > a and b > c:
    print(f'O maior é: {b}')
elif c > a and c > b:
    print(f'O maior é: {c}')
else:
    print('Existem numeros iguais!')

#UTILIZANDO OUTRO MÉTODO PARA ACHAR O MENOR:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor numero é: {menor}')