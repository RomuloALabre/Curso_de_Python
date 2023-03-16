#Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.
dist = int(input('Qual é a distância da sua viagem em KM? '))
if dist <= 200:
    vperto = dist * 0.5
    print(f'Sua viagem deve custar R$ {vperto:.2f}.')
else:
    vlonge = dist * 0.45
    print(f'Sua viagem custará R$ {vlonge:.2f}.')