# Um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'. Em que posição ela aparece a primeira vez. Em que posição aparece pela última vez.
frase = input('Escreva uma frase: ').strip().lower()
print(frase)
print('A quantidade de letra A é: ', frase.count('a'))
print('A posição que aparece a 1º vez: ', frase.find('a')+1)
print('Em qual posição aparece pela ultima vez: {}'.format(frase.rfind('a')+1))