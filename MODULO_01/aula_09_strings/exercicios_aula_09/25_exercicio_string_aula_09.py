# Crie um programa que leia o nome de uma pessoa e diga se tem "SILVA" no nome
nome = input('Digite seu nome completo: ')
print('Existe silva no seu nome? {}'.format('silva' in nome.lower()))