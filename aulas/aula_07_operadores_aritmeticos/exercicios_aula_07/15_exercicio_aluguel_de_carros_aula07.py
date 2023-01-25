# Escreva um programa que pergunto o KM e dias em que o carro esteve alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

d = int(input('Por quantos dias você alugou o carro? '))
k = int(input('Qual a quantidade total de KM rodados? '))

total = (d*60) + (k*0.15)

print(f'O custo total do aluguel do carro foi de: R$ {total:.2f}')