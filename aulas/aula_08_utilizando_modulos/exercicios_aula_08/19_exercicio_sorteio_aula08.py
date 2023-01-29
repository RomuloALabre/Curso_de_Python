# Um professor quer sortear um aluno. Faça um programa que ajude, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
al1 = str(input('Primeiro nome: '))
al2 = input('Segundo nome: ')
al3 = input('Terceiro nome: ')
al4 = input('Quarto nome: ')

lista = [al1, al2, al3, al4]
print(f'O(a) aluno(a) sorteado(a) foi: {choice(lista)}')
