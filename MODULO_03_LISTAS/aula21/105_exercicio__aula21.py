"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione tambem as docstrings da função
"""
def notas(*n, sit=False):
    men = mai = med = n[0]
    soma = 0
    for i in range(0 , len(n)):
        if men > n[i]:
            men = n[i]
        if mai < n[i]:
            mai = n[i]
        soma += n[i]
        med = soma / len(n)
    print(soma)
    r = dict()
    r['Total'] = len(n)
    r['Menor'] = men
    r['Maior'] = mai
    r['Média'] = med
    return r

#Programa Principal
resp = notas(5, 10, 2, 12, 1)
print(resp)