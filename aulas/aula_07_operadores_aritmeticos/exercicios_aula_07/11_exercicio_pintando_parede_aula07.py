larg = float(input('Insira o largura da parede em metros: '))
alt = float(input('Insira a altura da parede em metros: '))

área = alt*larg
tinta = área/2

print(f'A área da parede é de: {área}')
print(f'A quantidade de tinta necessária para pintar é: {tinta}litros')