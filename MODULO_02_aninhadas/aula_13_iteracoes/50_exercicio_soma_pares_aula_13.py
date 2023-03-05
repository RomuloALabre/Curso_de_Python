'''Desenvolva um programa que leia seis números inteiros e mostrea a soma apenas daqueles que foram pares. Se o valor digitado for impar, desconsidere-o.'''
soma = 0
cont = 0
for a in range(1 , 7):
    num = int(input(f'Digite o {a}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} números pares é: {soma}')
