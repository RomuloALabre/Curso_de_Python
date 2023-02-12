# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.
numa = int(input('Primeiro numero: '))
numb = int(input('Segundo numero: '))
numc = int(input('Terceiro numero: '))
if numa > (numb and numc):
    print(numa)
elif numb > (numa and numc):
    print(numb)
elif numc > (numa and numb):
    print(numc)
else:
    print('Existem numeros iguais!')