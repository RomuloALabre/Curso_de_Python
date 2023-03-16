# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. Módulo Math
from math import hypot
op = float(input('Digite a medida do cateto oposto: '))
ad = float(input('Digite o cateto adjacente: '))
h = hypot(op, ad)
print(f'A hipotenusa é: {h:.2f}')
