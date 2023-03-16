n = soma = 0
while True:
    n = int(input('Digite o valor que deseja somar:'))
    if n == 0:
        break
    soma += n
print(f'A soma é: {soma}')