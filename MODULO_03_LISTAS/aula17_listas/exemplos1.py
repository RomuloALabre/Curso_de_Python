valores = []
valores.append(3)
valores.append(6)
valores.append(9)

print(valores) #OU
for v in valores:
    #print(v) #OU
    print(f'{v} ', end='')

print('\nPara mostrar a posição junto com os valores:')
for c, v in enumerate(valores):
    print(f'Na posição {c} foi encontrado {v}!')