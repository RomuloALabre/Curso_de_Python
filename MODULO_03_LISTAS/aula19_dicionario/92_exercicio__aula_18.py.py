"""
 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
 acrescente, além da idade, com quantos anos a pessoa vai se aposentar.(35)
"""
from datetime import date
trabalho = dict()
trabalho['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trabalho['idade'] = date.today().year - nascimento
trabalho['CTPS'] = int(input('Nº Carteira de Trabalho (0 não tem): '))
if trabalho['CTPS'] > 0:
    trabalho['contratação'] = int(input('Ano de contratação: '))
    trabalho['salário'] = float(input('Salário: '))
    trabalho['aposentadoria'] = (trabalho['contratação'] + 35) - nascimento
else:
    print('Não possui emprego de carteira assinada.')
print('-='*30)
for k, v in trabalho.items():
    print(f' - {k} tem o valor: {v} ')
print()
    