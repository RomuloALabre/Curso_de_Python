try:
    a = int(input('Digite numerador: '))
    b = int(input('Digite dividendo: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou!')
except (ZeroDivisionError):
    print('Não é possível divisão por zero:')
except(KeyboardInterrupt): #se encerrar a operação
    print('O usuário não informou seus dados:')
except Exception as erro:
    print(f'Você cometeu um erro porque: {erro.__cause__}')

else:
    print(f'O resultado da divisão é: {r:.1f}')
finally:
    print('Volte sempre!')