#Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.
dist = int(input('Qual é a distância da sua viagem em KM? '))
vperto = dist * 0.5
vlonge = dist * 0.45
if dist <= 200:
    print(f'Sua viagem deve custar R$ {vperto:.0f},00.')
else:
    print(f'Sua viagem custará R$ {vlonge:.0f},00.')