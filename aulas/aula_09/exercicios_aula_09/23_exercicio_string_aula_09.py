# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados
# EX: 1834
# unidade 4, dezena 3, centena 8, milhar 1
num = int(input('Digite um numero: '[0000:9999]))
n = str(num)
print(f'A unidade é: ',n[3])
print(f'A dezena é: {n[2]}')
print('A centena é: ', n[1])
print('A milhar é: ', n[0])
# MELHOR FORMA
print('outra forma')
u = num // 1 % 10
d = num//10 %10
c = num//100 %10
m = num//1000 %10
print(f'A unidade é: {u}')
print(f'A dezena é: {d}')
print(f'A centena é: {c}')
print(f'A milhar é: {m}')