'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
a = float(input('Tamanho Reta A: '))
b = float(input('Tamanho Reta B: '))
c = float(input('Tamanho Reta C: '))
if a < b+c and b < a+c and c < a+b:
    print('Forma um triângulo! ', end='')
    if a == b == c:
        print('Triângulo equilátero.')
    elif a != b != c != a:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓCELES')
else:
    print('NÃO forma Triângulo.')