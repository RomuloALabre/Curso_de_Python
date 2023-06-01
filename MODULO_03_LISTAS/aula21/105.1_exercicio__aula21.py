'''
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione tambem as docstrings da função
'''
def notas(*n, sit=False):
    '''
    --> Analisar as notas da turma.
    - param n: uma ou mais notas de alunos
    - param sit: (opcional) mostrar ou não situação da média da turma
    - return: Dicionário com todas inf da turma
    '''
    r = dict()
    r['Total'] = len(n)
    r['Menor'] = min(n)
    r['Maior'] = max(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 8:
            r['Situação'] = 'Ótimo'
        elif 6 <= r['Média'] < 8:
            r['Situação'] = 'Good'
        else:
            r['Situação'] = 'Ruim'
    return r

#Programa Principal
resp = notas(5, 10, 6, 12, 9, sit=True)
help(notas)
print(resp)
