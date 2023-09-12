"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

o 'diminuir()', mesma coisa.

"""
import moeda
preço = float(input('Digite um valor: R$ '))
taxa = float(input('Insira a taxa: '))
print(f'O preço R$ {preço}  com uma taxa de {taxa}% fica um total de: R$ {moeda.aumentar(preço, taxa)}')

print(f'O preço R$ {preço} com taxa de desconto de {taxa}% o valor fica: R$ {moeda.diminuir(preço, taxa)}')

print(f'O dobro do preço é: R$ {moeda.dobro(preço)}')

print(f'A metade do preço é: R$ {moeda.metade(preço)}')