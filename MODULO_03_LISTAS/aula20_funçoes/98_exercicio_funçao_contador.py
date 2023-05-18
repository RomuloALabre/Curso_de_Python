"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem
Seu programa tem que realizar três contagens através da função criada
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada
--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""
from time import sleep
def contador(i , f , p):
    print('-='*20)
    #Tratamento de erros
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contador de {i} até {f}, de {p} em {p}')
    sleep(1)
    if i < f:
        while i <= f:
            print(f'{i}, ', end='', flush=True)
            sleep(0.3)
            i += p
        print('Fim!')
    else:
        while i >= f:
            print(f'{i}, ', end='', flush=True)
            sleep(0.3)
            i -= p
        print('Fim!')

# Programa principal
contador(1 , 10 , 1)
contador(10, 0, 2)
print('-='*20)
print('Escolha a forma de contagem: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
