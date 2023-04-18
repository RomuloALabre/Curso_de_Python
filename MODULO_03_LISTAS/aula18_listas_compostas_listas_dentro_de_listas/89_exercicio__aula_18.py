"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente
"""
"""
Serão 3 níveis de lista dentro de uma única
Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""
aluno = 0
notas = list()
lista = list()
listafinal = list()
cadastro = cont = 0
nota1 = nota2 = media = 0
while True:
    cadastro = str(input('Deseja cadastrar um aluno? ')).upper().strip()[0]
    if cadastro != 'N':
        aluno = str(input('Nome:'))
        nota1 = float(input('Nota1: '))
        nota2 = float(input('Nota2: '))
        media = (nota1 + nota2) / 2
        lista.append([aluno, [nota1 , nota2], media])
        cont += 1      
    else:
        break
print('-='*30)
print('BOLETIM ESCOLAR')
print(f'{"Nº":<4}{"ALUNO":<10}{"MEDIA":>8}')
print('-'*26)

for c in range(0 , cont): #PODE SER SUBSTITUÍDO PELO 'for i , a in enumerate (lista)'
    print(f'{c:<4}', end='')
    print(f'{lista[c][0]:<10}',end=' ')
    print(f'{lista[c][2]:>8}')
while True:
    consulta = int(input('Digite o número do aluno, para consulta: '))
    if consulta == 999:
        break
    else:
        print(f'O aluno {lista[consulta][0]} tem notas {lista[consulta][1]}')
print('Programa finalizado!')