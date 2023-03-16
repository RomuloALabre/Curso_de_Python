"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
cin = vint = dez = um = 0
print('='*30,'BANCO RAL','='*30)
while True:
    saque = int(input('Digite o valor que deseja sacar: '))
    if saque >= 50:
        cin = saque // 50
        print(f'{cin} notas de R$ 50,00')
    saque = saque - (50 * cin)
    if saque >= 20:
        vint = saque // 20
        print(f'{vint} notas de R$ 20,00')
    saque = saque - (20 * vint)
    if saque >= 10:
        dez = saque // 10
        print(f'{dez} notas de R$ 10,00')
    saque = saque - (10 * dez)
    if saque >= 1:
        um = saque // 1 
        print(f'{um} notas de R$ 1,00')
    break