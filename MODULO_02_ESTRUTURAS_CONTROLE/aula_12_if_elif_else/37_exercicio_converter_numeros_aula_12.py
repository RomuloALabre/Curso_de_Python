''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
num = int(input('Digite um número inteiro para converter: '))
print('''Escolha a base para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
[ 4 ] todas as opções\n''')
opcao = int(input('Qual opção você deseja? '))
if opcao == 1:
    print(f'{num} convertido para binário é igual a: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O numero {num} convertido para OCTAL é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
elif opcao == 4:
    print(f'''
    Em BINÁRIO: {bin(num)} 
    Em HEXADECIMAL: {hex(num)}
    Em OCTAL: {oct(num)}''')
else:  
    print('Seleção inválida, tente novamente!')
