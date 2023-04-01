print('Uma lista atribuída a outra, elas permanecem ligadas e com valores iguais entre elas. Veja!')
a = [2, 4, 6, 8]
b = [3, 5, 7, 9]
b = a
b[2] = 10 # Para mostrar que tudo que altera em A será alterado em B e vice versa!
print('Ambas se tornaram iguais: Veja!')
print(f'Lista A: {a}\nLista B: {b}')

'''Já se eu criar B desta forma, eles não terão ligação, veja!'''
a = [2, 4, 6, 8]
b = a[:]
b[2] = 10
print('\nAmbas podem ser editáveis separadamente: Veja!')
print(f'Lista A: {a}\nLista B: {b}')