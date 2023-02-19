# Um professor quer sortear a ordem das apresentações de trabalhos dos alunos. Faça um programa que leia o nome de 4 grupos e mostre a ordem sorteada.
from random import shuffle
al1 = input('Digite o nome de um aluno: ')
al2 = input('Digite o nome de um aluno: ')
al3 = input('Digite o nome de um aluno: ')
al4 = input('Digite o nome de um aluno: ')

lista = [al1, al2, al3, al4]

shuffle(lista)

print(f'A ordem de apresentação será: {lista}')