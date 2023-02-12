# Pergunte o salário e calcule o preço de um aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Insira o salário: '))
min = sal * (10/100)
max = sal * (15/100)
if sal <= 1250:
    print(f'Novo salário com 10% de aumento: R$ ',min + sal)
else:
    print(f'Salário com 15%: R$ ',max + sal)