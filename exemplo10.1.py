def parImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Numero: '))
if parImpar(num):
    print('é Par')
else:
    print('Ímpar')
    