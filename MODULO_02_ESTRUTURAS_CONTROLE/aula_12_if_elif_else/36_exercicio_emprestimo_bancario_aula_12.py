'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar
Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
print('Vamos analisar o seu crédito para empréstimo.')
vcasa = float(input('Qual é o valor do imóvel que deseja comprar? '))
salario = float(input('Qual é o seu salário atual? R$ '))
ano = int(input('Em quantos anos deseja pagar? '))
prest = vcasa / (ano * 12)
if prest >= (30 * salario)/100:
    print('Você não possui margem para o empréstimo. Tente aumentar o tempo para amortização.')

else:
    print(f'Empréstimo liberado com prestações mensais no valor de R${prest:.2f} mensais')