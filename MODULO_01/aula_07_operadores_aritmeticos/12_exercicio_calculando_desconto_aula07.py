preço = float(input('Insira o valor do produto: '))
desc = int(input('Insira o valor de desconto: '))

t = (preço * desc) /100

vf = preço-t

print(f'valor inicial: R$ {preço:.2f}\nvalor do desconto: {desc}%\npreço final com desconto: R$ {vf:.2f}')