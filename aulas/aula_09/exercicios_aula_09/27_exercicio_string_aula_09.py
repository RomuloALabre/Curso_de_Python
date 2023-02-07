# Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeior e o último nome separadaente.
nome = input('Digite seu nome: ').strip()
divide = nome.split()
print('Primeiro nome: {}'.format(divide[0][0:]))
print('Segundo nome: {}'.format(divide[len(divide)-1]))
