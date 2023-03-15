#   Exercício Python 062 - Super Progressão Aritmética v3.0
#   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#   O programa encerrará quando ele disser que quer mostrar 0 termos.
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
qtd = int(input('Qtd termos: '))
c = 0
cont = 1
while c < qtd:
    print(termo)
    termo += razao
    c += 1
    if c == qtd and qtd != 0:
        print('pausa')
        print('Deseja continuar? Pressione 0 para sair')
        qtd = int(input('Qual é a qtd de termos: '))
        c = 0
        if qtd == 0:
            print('Sair do programa!')