'''Crie um programa que leia uma frase qualquer e diga se ela é um **polindromo, desconsiderando os espaços.'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto}, é {inverso}')
if inverso == junto:
    print('é um palímdromo')
else:
    print('Não é palíndromo')
'''OU
inverso = junto[::-1]'''