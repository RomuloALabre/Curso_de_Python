"""
 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.
 EX:
 Nome: Glaucia
 Media da Glaucia: 8.5
 Nome é igual a Glaucia
 Média é igual a : 8.5
 Situação é igual a Aprovado
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
