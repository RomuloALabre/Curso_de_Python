#   Exercício Python 065 - Maior e Menor valores
#   Crie um programa que leia vários números inteiros pelo teclado.
#   No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#   O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = cont = soma = 0
resp = 'S'
maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número que deseja calcular: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num <= menor:
            menor = num
    soma = soma + num
    cont += 1
    resp = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
media = soma / cont
print(f'A media é: {media}')
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')