#Desenvolva um programa que leia o comprimento de 3 retas, e diga ao usuário se elas podem formar um triângulo ou não.
a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))
tri = (a + b + c)% 3 
if tri == 0:
    print('Forma um triangulo!')
else:
    print('Não forma um triângulo:')