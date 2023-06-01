"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""
def voto(nasc=0, year=0):
    from datetime import date
    year = date.today().year
    nasc = year - nasc
    if 0 < nasc < year:
        print(f'Você tem {nasc} anos, seu voto é ', end='')
        if 16 <= nasc < 18 or nasc >= 65:
            print('OPCIONAL')
        elif nasc >= 18:
            print('OBRIGATÓRIO')
        else:
            print('NÃO PERMITIDO PARA SUA IDADE')
    else:
        print('Data inválida, tente novamente!')
        #return True ???


#Programa Principal
voto(int(input('Digite seu ano de nascimento: ')))
