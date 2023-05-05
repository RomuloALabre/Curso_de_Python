"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(alt , larg):
    area = alt * larg
    print(f'A altura é {alt} a largura é {larg}, área total do terreno é: {area} m².')


#Programa principal
print('Controle de Terreno')
print('-'*20)

a = float(input('ALTURA: '))
l = float(input('LARGURA: '))
area(a , l)
