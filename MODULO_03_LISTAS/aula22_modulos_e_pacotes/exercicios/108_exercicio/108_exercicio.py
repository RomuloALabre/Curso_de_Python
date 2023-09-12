"""
Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.
"""
import moeda
preço = float(input('Digite um valor: R$ '))
taxa = float(input('Insira a taxa: '))
print(f'O preço {moeda.moeda(preço)}  com uma taxa de {taxa:.0f} % fica um total de: {moeda.moeda(moeda.aumentar(preço, taxa))}')

print(f'O preço {moeda.moeda(preço)} com taxa de desconto de {taxa}% o valor fica: {moeda.moeda(moeda.diminuir(preço, taxa))}')

print(f'O dobro do preço é: {moeda.moeda(moeda.dobro(preço))}')

print(f'A metade do preço é: {moeda.moeda(moeda.metade(preço))}')