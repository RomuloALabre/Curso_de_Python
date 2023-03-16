n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Agora digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média é: {m}')
if m >= 7:
    print('Você foi aprovado')
else:
    print('infelizmente você foi reprovado, estude mais!')

#ou
print('PARABÉNS!' if m >= 9 else 'Continue se esforçando!')