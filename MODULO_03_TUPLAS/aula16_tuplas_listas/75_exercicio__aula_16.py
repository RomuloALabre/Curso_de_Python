'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''
valor = (int(input('Digite o valor: ')), 
         int(input('Digite o segundo valor: ')), 
         int(input('Digite o terceiro valor: ')), 
         int(input('Digite o quarto valor: ')))
print(valor)
print(f'A quantidade de vezes o número "nove" aparece foi: {valor.count(9)}')
if 3 in valor:
    print(f'O primeiro valor "três" foi na posição: {valor.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print('Os valores PARES digitados: ',end='')
for v in valor:
    if v % 2 == 0:
        print(v, end=', ')



