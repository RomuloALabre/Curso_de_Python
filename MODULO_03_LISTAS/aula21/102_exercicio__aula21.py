"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(n=0, show=False):
    '''
    --> Calcula o fatorial de um número.
    - param n: o número a ser calculado
    - param show: (opcional) mostrar ou não a conta
    - return: O valor total do fatorial de um número número
    '''
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(f'{c} x', end=' ')  
            else:
                print(f'{c} =', end=' ') 
        f *= c
    return f

#Programa Principal
help(fatorial)
print(fatorial(5, show=True))

