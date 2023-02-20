'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
idade = int(input('Qual é a sua idade? '))
if idade < 17:
    print('Ainda não está na hora do seu alistamento. Aguarde!')
elif idade > 18:
    print('Você já passou da idade de alistamento, procure uma junta militar para regularizar o seu certificado de reservista.')
else:
    print('Faça o seu alistamento clicando no botão abaixo.')