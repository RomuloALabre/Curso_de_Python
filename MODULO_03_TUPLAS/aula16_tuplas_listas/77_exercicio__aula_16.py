'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''
nomes = ("Galadriel", "Luthien Tinuviel", "Erik Killmonger", 
        "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda")
for palavra in nomes: # Para cada PALAVRA em lista NOMES
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra: # Para cada LETRA em PALAVRA
        if letra.lower() in 'aeiou': # Se letra está em aeiou
            print(letra.upper(), end=', ')  