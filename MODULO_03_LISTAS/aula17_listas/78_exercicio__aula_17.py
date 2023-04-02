'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
valores = list()
for v in range(0 , 5):
    valores.append(int(input(f'Digite o {v+1}º valor para a lista: ')))
print(f'Você digitou os valores {valores}')
print(f'O menor valor da lista é: {min(valores)} e está na posição {valores.index(min(valores))+1}')   
print(f'O maior valor da lista é: {max(valores)} e está na posição {valores.index(max(valores))+1}')