'''Crie uma programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
for n in range(0,51):
    if n % 2 == 0:    
        print(f'{n} É um número par')
    else:
        print(f'{n} É um número ímpar')
     
#OU resolução do professor
for n in range(0 , 51, 2):
    print(f'{n} É um número par.')