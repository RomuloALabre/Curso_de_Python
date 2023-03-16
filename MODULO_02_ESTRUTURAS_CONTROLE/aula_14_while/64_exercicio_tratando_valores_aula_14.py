#   Exercício Python 064 - Tratando diversos valores
#   Crie um programa que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#   No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag "999").
c = 0
soma = 0
while c >= 0:
    num = int(input('Digite o número que deseja [999 para parar]: '))
    if num == 999:
        break
    soma = soma + num
    c += 1  
print(f'Você digitou {c} números.')
print(f'E a soma é: {soma}')