#   Exercício Python 057 - Validação de Dados
#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor tente novamente! \nDigite o sexo M/F:')).upper().strip()[0]
if sexo == 'F':
    print('Você digitou sexo FEMININO.')
else:
    print('Você digitou sexo MASCULINO.')