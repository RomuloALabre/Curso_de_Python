"""
Adicione ao módulo moeda.py, criado nos exercícios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
from moeda import moeda
preço = float(input('Digite um valor: R$ '))
#taxaa = float(input('Insira a taxa: '))
moeda.resumo(preço, 30, 10)

'''
print(f'O preço de {moeda.moeda(preço)} com uma taxa de {taxa:.0f} % fica um total de: {(moeda.aumentar(preço, taxa, True))}')

print(f'O preço {moeda.moeda(preço)} com taxa de desconto de {taxa}% o valor fica: {(moeda.diminuir(preço, taxa, True))}')

print(f'O dobro do preço é: {(moeda.dobro(preço, True))}')

print(f'A metade do preço é: {(moeda.metade(preço, True))}')
'''