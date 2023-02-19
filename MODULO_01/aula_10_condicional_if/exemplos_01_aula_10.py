tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Seu carro é novo')
else:
    print('Seu carro é usado')
print('--FIM--')
#ou
print('Carro novo'if tempo<=3 else'carro velho')