#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#   Só que agora o jogador vai tentar adivinhar até acertar, #   mostrando no final
#   quantos palpites foram necessários para vencer.
from random import randint
sorteio = randint(1 , 10)
num = 0
count = 0
print('Sou seu computador e pensei num número, será que você consegue adivinhar? ')
while num != sorteio:
    if count > 0:
        if num < sorteio:
            print(f'O número que pensei é Maior que {num}')
        else:
            print(f'O número que pensei é Menor que {num}')
    num = int(input('Escolha um número: '))
    count += 1
print(f'Parabéns, você acertou!\nVocê utilizou {count} tentativas.')
