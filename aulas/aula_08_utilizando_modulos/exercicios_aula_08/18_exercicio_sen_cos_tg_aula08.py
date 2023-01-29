# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
num = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
 
print(f'O seno: {sen:.2f}, \ncosseno: {cos:.2f}, \nE a tangente é: {math.tan(math.radians(num))}')