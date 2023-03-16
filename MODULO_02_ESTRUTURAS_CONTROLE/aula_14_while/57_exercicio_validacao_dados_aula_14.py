#   Exercício Python 057 - Validação de Dados
#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = 0
while (sexo != 'M' and sexo != 'F'):
    if sexo != 0:
        print('Dados inválidos, por favor tente novamente!')
    sexo = str(input('Digite o sexo M/F:')).upper().strip()[0]
if sexo == 'F':
    print('Você digitou sexo FEMININO.')
else:
    print('Você digitou sexo MASCULINO.')