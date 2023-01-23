p = float(input('Insira o valor do produto: '))
d = int(input('Insira o valor de desconto: '))

t = (p * d)/100

vf = p-t

print(f'valor inicial: {p}\nvalor do desconto: {d}%\npreço final com desconto: {vf}')