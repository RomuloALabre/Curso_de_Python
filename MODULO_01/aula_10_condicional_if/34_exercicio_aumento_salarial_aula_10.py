# Pergunte o salário e calcule o preço de um aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Insira o salário: '))
menor = sal * (15/100)
maior = sal * (10/100)
if sal <= 1250:
    print(f'Novo salário com 10% de aumento: R$ ',menor + sal)
else:
    print(f'Salário com 15%: R$ ',maior + sal)