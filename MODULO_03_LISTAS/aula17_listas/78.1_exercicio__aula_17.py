'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
# RESOLUÇÃO COM O PROFESSOR
valores = []
min = 0
max = 0
for v in range(0 , 5):
    valores.append(int(input(f'Digite o {v+1}º valor: ')))
    if v == 0:
        min = max = valores[v]
    else:
        if valores[v] < min:
            min = valores[v]
        if valores[v] > max:
            max = valores[v]
print(f'Os valores digitados foram {valores}')
print(f'O menor valor digitado foi: {min} e está nas posições: ', end='')
for i , c in enumerate(valores):
    if c == min:
        print(f'{i+1}...', end='')  
print()
print(f'O maior valor digitado foi: {max} e está nas posições: ', end='')
for j , c in enumerate(valores):
    if c == max:
        print(f'{j+1}...', end='')