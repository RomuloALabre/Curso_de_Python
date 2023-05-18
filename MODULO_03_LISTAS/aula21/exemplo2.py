def somar(a, b, c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(2, 4, 6)
somar(2, 4) #sem o c=0 daria um erro , devido falta de parametro
somar(a=2, b=0, c=3)