'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros no valor total
'''

print('{:=^40}'.format('Lojas ALVES'))
preco = float(input('Qual é o valor do produto? '))
print('''Escolha uma das formas de pagamento abaixo: \n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão''')
opcao = int(input('Escolha a sua opção de pagamento: '))
if opcao == 1:
    total1 = preco - (preco * 0.1)
    print(f'Você receberá 10% de desconto, o pagamento à vista será de: R$ {total1:.2f}')
elif opcao == 2:
    total2 = preco - (preco * 0.05)
    print(f'Você receberá 5% de desconto, o pagamento à vista no cartão será de: R$ {total2:.2f}')
elif opcao == 3:
    print(f'Valor do produto a ser pago: R$ {preco:.2f}')
elif opcao == 4:
    total3 = preco + (preco * 0.2)
    prest = int(input('Em quantas parcelas deseja pagar? '))
    parc = total3 / prest
    print(f'Valor total parcelado: R$ {total3:.2f}')
    print(f'Com prestações em {prest}x de R$ {parc:.2f}')
else:
    print('Opção inválida, tente novamente!')
print('\nOBRIGADO PELA PREFERÊNCIA!\n')


                                                                                                                                                                                    