#Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80KM/h, mostre a mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite.
veloc = int(input('Velocidade do veículo: '))
multa = (veloc-80) * 7
if veloc > 80:
    print(f'Você foi multado em R$ {multa},00')
else:
    print('Você passou dentro do limite de velocidade permitida de 80 KM/H.')
    print('Dirija com segurança!')
    