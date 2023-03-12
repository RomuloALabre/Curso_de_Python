#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Crie um programa que leia dois valores e mostre um menu na tela:
#       [ 1 ] somar
#       [ 2 ] multiplicar
#       [ 3 ] maior
#       [ 4 ] novos números
#       [ 5 ] sair do programa
#   Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
result = 0
opcao = 0
while opcao >= 0 and opcao < 5: 
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('Escolha uma das operações que deseja realizar: '))
    if opcao == 1:
        result = valor1 + valor2
        print(f'A soma dos valores é: {result}')
    elif opcao == 2:
        result = valor1 * valor2
        print(f'A multiplicação desses valores é: {result}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O valor {valor1} é maior que {valor2}')
        else:
            print(f'O valor {valor2} é maior que {valor1}')
    elif opcao == 4:
        print('Escolha outros valores: ')
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))        
    sleep(2)
print('Você saiu do programa.')