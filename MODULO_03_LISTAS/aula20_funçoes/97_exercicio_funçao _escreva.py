"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.
Ex:
escreva("Olá, Mundo!")
Saída:
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
~~~~
PTH
~~~~
"""
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa principal
texto = (str(input('Digite seu texto: ')))
escreva(texto)
