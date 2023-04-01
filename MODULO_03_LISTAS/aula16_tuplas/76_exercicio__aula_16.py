'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência
No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''
lista = ("pão", 1.20,
        "leite", 3.50,
        "frango", 10.90)
print("=" * 40)
print(f'{"Lista de Preços":^40}')
print("=" * 40)
for pos in range(0 , len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('=' * 40)