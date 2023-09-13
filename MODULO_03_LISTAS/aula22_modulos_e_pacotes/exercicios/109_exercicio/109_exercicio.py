"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvido no desafio 108.
"""
import moeda
preço = float(input('Digite um valor: R$ '))
taxa = float(input('Insira a taxa: '))
print(f'O preço de {moeda.moeda(preço)} com uma taxa de {taxa:.0f} % fica um total de: {(moeda.aumentar(preço, taxa, True))}')

print(f'O preço {moeda.moeda(preço)} com taxa de desconto de {taxa}% o valor fica: {(moeda.diminuir(preço, taxa, True))}')

print(f'O dobro do preço é: {(moeda.dobro(preço, True))}')

print(f'A metade do preço é: {(moeda.metade(preço, True))}')