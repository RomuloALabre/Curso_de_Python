'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
import datetime
ano = int(input('Digite o ano de nascimento do(a) atleta: '))
data = datetime.date.today()
anoatual = data.year
idade = anoatual - ano
print(f'Você tem {idade} anos.')
if ano > anoatual:
    print('Data inválida.')
elif idade <= 9:
    print('Você está na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil.')
elif idade > 14 and idade <= 19:
    print('Categoria Júnior.')
elif idade > 19 and idade <= 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
