#Crie um programa que leia o nome de uma pessoa e mostre:
# 1 O nome com todas as letras maiúculas
# 2 O nome com todas minúsculas
# 3 Quantas letras ao todo sem considerar espaços
# 4 Quantas letras tem o primeiro nome

nome = input('Digite seu nome:').strip()
print('Em maiuscula é: ',nome.upper())
print('Em minuscula é: ',nome.lower())
print('A quantidade de letras: {} letras'.format(len(nome.replace(" ",""))))
print('O primeiro nome tem: {} letras' .format(nome.find(' ')))
#ou
separa = nome.split()
print('O primeiro nome {} tem: {} letras' .format(separa[0] ,len(separa[0])))